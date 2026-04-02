
-- rd_headless_bridge.lua
-- Automated bridge for RetroDiffusion headlessly via Aseprite

local rd_path = "/Users/michaelraftery/Library/Application Support/Aseprite/extensions/RetroDiffusion/"
local prompt = app.params["prompt"]
local output = app.params["output"]
local width = tonumber(app.params["width"]) or 16
local height = tonumber(app.params["height"]) or 16

if not prompt or not output then
    print("FAIL: Missing prompt or output parameters")
    app.exit()
    return
end

print("RD_BRIDGE: Initializing for prompt: " .. prompt)

-- 1. Mock UI components to prevent headless crashes
if not app.isGui then
    Dialog = function(title)
        local d = {}
        function d:label() return self end
        function d:button() return self end
        function d:entry() return self end
        function d:slider() return self end
        function d:check() return self end
        function d:separator() return self end
        function d:canvas() return self end
        function d:show() end
        function d:close() end
        function d:repaint() end
        function d:modify() end
        d.data = { zoom = 1 }
        d.bounds = { x=0, y=0, width=0, height=0 }
        return d
    end
end

-- 2. Load RetroDiffusion Logic
local generator = dofile(rd_path .. "scripts/generator.lua")

-- 3. Configure Parameters
local gMode = "txt2img"
local gDevice = true -- true for CPU
local gOptimized = true
local gPrecision = "fp32"
local modelFolder = rd_path .. "stable-diffusion-aseprite/models/"
local loraFolder = rd_path .. "stable-diffusion-aseprite/models/lora/"
local loraFiles = {}
local loraWeights = {}
local gPixelSize = 1
local gMaxBatchSize = 1
local gParameters = {
    prompt = prompt,
    negative_prompt = "blurry, low quality, 3d, gradient, shadow",
    steps = 20,
    guidance_scale = 7.0,
    saveas = "layers",
    preview = false,
    iter = 1
}
local gLighting = { enabled = false }
local gComposition = { enabled = false }
local gSeed = -1
local nets = {}

-- 4. Trigger Generation
if not app.activeSprite then
    local s = Sprite(width, height)
    print("RD_BRIDGE: Created temporary sprite " .. width .. "x" .. height)
end

generator:Create(gMode, gDevice, gOptimized, gPrecision, modelFolder, loraFolder, loraFiles, loraWeights, gPixelSize, gMaxBatchSize, width, height, gParameters, gLighting, gComposition, gSeed, nets)

-- 5. Wait for Result
print("RD_BRIDGE: Generation started (CPU mode)...")
local timeout = 600
local elapsed = 0
while generator:Check() and elapsed < timeout do
    local t = os.clock()
    while os.clock() - t < 1 do end 
    elapsed = elapsed + 1
    if elapsed % 10 == 0 then
        print("RD_BRIDGE: Waiting... " .. elapsed .. "s")
    end
end

if elapsed >= timeout then
    print("FAIL: Generation timed out")
    app.exit()
    return
end

-- 6. Save and Exit
if app.activeSprite then
    app.activeSprite:saveAs(output)
    print("SUCCESS: Image saved to " .. output)
else
    print("FAIL: No sprite generated")
end

app.exit()
