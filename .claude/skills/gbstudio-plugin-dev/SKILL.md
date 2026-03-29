---
name: gbstudio-plugin-dev
description: Guide for writing Custom Event Plugins (.js) and Engine Plugins (C) for GB Studio 4.2.2. Use when asked to create a new visual block for the editor or when fixing plugin compilation errors like "Didn't expect to get here".
---

# GB Studio 4.2.2 Plugin Development Guide

This skill provides the architectural rules and helper signatures for building custom plugins in GB Studio 4.2.x.

## Folder Structure (Strict)
Plugins must be placed in a named subfolder within the root `plugins/` directory.

- **Script Event Plugins (.js):** `plugins/[YourPluginName]/events/eventMyCustomEvent.js`
  *(Must start with `event`)*
- **Engine Plugins (.c):** `plugins/[YourPluginName]/engine/src/my_code.c`
  *(Must include an `engine.json` file)*

## Fixing Engine Version Warnings
If the compiler throws: *Plugin is based on an unknown engine version*, you must create or update `plugins/[YourPluginName]/engine/engine.json` with:
```json
{
  "version": "4.2.2-e1",
  "fields": []
}
```

## The "Didn't Expect To Get Here" Crash (eval.js)
This fatal error occurs when a `.js` plugin uses outdated helper signatures during the `compile` step. GB Studio 4.x refactored many helpers.

### Rule 1: Single-Argument Activation
Do not pass multiple arguments to `actorSetActive`.
**Correct:** `actorSetActive(input.actorId);`

### Rule 2: 3-Argument Movement Helpers
Older versions passed the Actor ID to movement helpers. In 4.x, the engine assumes the "Active" actor is moving.
**WRONG (Will Crash):** `actorMoveTo(input.actorId, x, y, true);`
**CORRECT:** 
```javascript
actorSetActive(input.actorId);
actorMoveTo(x, y, true); // or actorMoveToScriptValues(x, y, true);
```
*(Signature: `x`, `y`, `useCollisions`)*

## Emitting GBVM Assembly
When your plugin needs to bypass standard helpers and emit raw GBVM:
```javascript
const compile = (input, helpers) => {
    const { _addComment, _addNL, _addInstruction } = helpers;
    
    _addComment("Start Raw GBVM");
    _addInstruction("VM_PUSH_CONST", 10);
    _addNL();
};
```