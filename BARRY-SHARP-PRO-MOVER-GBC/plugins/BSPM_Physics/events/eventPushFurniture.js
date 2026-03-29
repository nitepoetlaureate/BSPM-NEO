const id = "BSPM_EVENT_PUSH_FURNITURE";
const groups = ["Barry Sharp", "Physics"];
const name = "Push Furniture (Grid-Aligned)";

const fields = [
    {
        key: "actorId",
        label: "Furniture Actor",
        type: "actor",
        defaultValue: "$self$"
    }
];

const compile = (input, helpers) => {
    const { _addComment, actorSetActive, actorMoveTo } = helpers;
    
    _addComment("Start Push Furniture");
    
    // 4.2.2 helper: actorSetActive only takes one argument
    actorSetActive(input.actorId);
    
    // 4.2.2 helper: actorMoveTo(x, y, useCollisions)
    actorMoveTo(12, 10, true);
    
    _addComment("End Push Furniture");
};

module.exports = {
    id,
    name,
    groups,
    fields,
    compile
};
