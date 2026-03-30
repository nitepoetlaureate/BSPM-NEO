const id = "BSPM_EVENT_PUSH_FURNITURE";
const groups = ["Barry Sharp", "Physics"];
const name = "Push Furniture (Grid-Aligned)";

const fields = [
    {
        key: "actorId",
        label: "Furniture Actor",
        type: "actor",
        defaultValue: "$self$"
    },
    {
        key: "distance",
        label: "Push Distance (Tiles)",
        type: "number",
        defaultValue: 1,
        min: 1,
        max: 5
    }
];

const compile = (input, helpers) => {
    const { _addComment, actorSetActive, appendRaw, _declareLocal, _stackPop } = helpers;
    
    _addComment("Start Push Furniture (Dynamic Math)");
    
    // 1. Get Player Direction (Actor 0) into a local
    const dirVar = _declareLocal();
    appendRaw(`VM_ACTOR_GET_DIR 0, ${dirVar}`);
    
    // 2. Set active actor to the target furniture
    actorSetActive(input.actorId);
    
    // 3. Get current position of target actor into locals
    const xVar = _declareLocal();
    const yVar = _declareLocal();
    appendRaw(`VM_ACTOR_GET_POS 0, ${xVar}, ${yVar}`);
    
    // Calculate distance in subpixels (1 tile = 8 pixels = 128 subpixels)
    const moveAmount = input.distance * 128;
    
    _addComment("Directional Logic");

    // Right (1)
    appendRaw(`VM_IF_CONST .NE, ${dirVar}, 1, 1$, 0`);
    appendRaw(`VM_RPN`);
    appendRaw(`    .R_REF ${xVar}`);
    appendRaw(`    .R_INT16 ${moveAmount}`);
    appendRaw(`    .R_OPERATOR .ADD`);
    appendRaw(`    .R_STOP`);
    _stackPop(xVar);
    appendRaw("VM_JUMP 5$");
    appendRaw("1$:");

    // Left (2)
    appendRaw(`VM_IF_CONST .NE, ${dirVar}, 2, 2$, 0`);
    appendRaw(`VM_RPN`);
    appendRaw(`    .R_REF ${xVar}`);
    appendRaw(`    .R_INT16 ${moveAmount}`);
    appendRaw(`    .R_OPERATOR .SUB`);
    appendRaw(`    .R_STOP`);
    _stackPop(xVar);
    appendRaw("VM_JUMP 5$");
    appendRaw("2$:");

    // Up (4)
    appendRaw(`VM_IF_CONST .NE, ${dirVar}, 4, 3$, 0`);
    appendRaw(`VM_RPN`);
    appendRaw(`    .R_REF ${yVar}`);
    appendRaw(`    .R_INT16 ${moveAmount}`);
    appendRaw(`    .R_OPERATOR .SUB`);
    appendRaw(`    .R_STOP`);
    _stackPop(yVar);
    appendRaw("VM_JUMP 5$");
    appendRaw("3$:");

    // Down (8)
    appendRaw(`VM_IF_CONST .NE, ${dirVar}, 8, 4$, 0`);
    appendRaw(`VM_RPN`);
    appendRaw(`    .R_REF ${yVar}`);
    appendRaw(`    .R_INT16 ${moveAmount}`);
    appendRaw(`    .R_OPERATOR .ADD`);
    appendRaw(`    .R_STOP`);
    _stackPop(yVar);
    appendRaw("4$:");

    appendRaw("5$:");
    _addComment("Move to calculated X/Y");
    // VM_ACTOR_MOVE_TO <actor_idx> <x_var> <y_var>
    appendRaw(`VM_ACTOR_MOVE_TO 0, ${xVar}, ${yVar}`);
    _addComment("End Push Furniture");
};

module.exports = {
    id,
    name,
    groups,
    fields,
    compile
};
