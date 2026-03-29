---
name: gbstudio-4-2-migration
description: Guide for migrating or structuring GB Studio projects to the 4.2.x distributed .gbsres format. Use when project files fail to load, when the user reports "migration" loops, or when generating new scenes/assets programmatically.
---

# GB Studio 4.2.2 Migration & Structure Guide

This skill provides the architectural rules for working with GB Studio 4.2.x projects. 

## The Core Shift: Monolithic vs. Distributed
Older versions of GB Studio (3.x and 4.1) stored the entire game's logic, scenes, and variables in a single, massive JSON file called `project.gbsproj`.

**GB Studio 4.2+ uses a distributed resource model.**
The `project.gbsproj` is now just a tiny pointer file. All actual data lives in individual `.gbsres` files.

## Directory Structure
When generating or modifying a 4.2 project, you must adhere to this structure:

```text
[Project Root]/
├── project.gbsproj (Must specify "_version": "4.2.x" or higher)
├── assets/
│   ├── backgrounds/ (Images + .png.gbsres metadata)
│   ├── sprites/     (Images + .png.gbsres metadata)
│   └── custom_events/ (Where .gbsres custom UI events live)
└── project/
    ├── scenes/      (Folders for each scene, e.g., scene_1/scene.gbsres)
    ├── scripts/     (Distributed engine scripts)
    ├── palettes/    (.gbsres palette definitions)
    ├── settings.gbsres
    └── variables.gbsres
```

## Solving "Migration Loops"
If a user reports that their project keeps asking them to "migrate" or that custom files/plugins keep disappearing when they open the GUI:
1. **Diagnosis:** The `project.gbsproj` is likely specifying an older `_version` (like `"3.1.0"`). When the GUI sees this, it rewrites the `project/` directory, deleting files that aren't registered in the old format.
2. **The Fix:**
   - Close the GUI.
   - Set the `_version` in `project.gbsproj` to `"4.1.0"` (the last pre-distributed version).
   - Delete the broken `project/` folder if corrupted.
   - Reopen the GUI and let it perform a clean migration to 4.2.2.

## Custom Events vs. Plugins
- **Visual Custom Events** (created in the UI) are stored in `assets/custom_events/name.gbsres`.
- **Script Event Plugins** (written in JavaScript to add new blocks to the UI) are stored in `plugins/[CategoryName]/events/eventName.js`.
