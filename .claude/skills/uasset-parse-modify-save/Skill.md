---
name: uasset-parse-modify-save
description: Use when users need to parse, modify, or save Unreal .uasset files with UAssetAPI scripts, including batch readability checks and targeted property edits.
version: 1.0.0
---

# UAsset Parse Modify Save

## Overview

This Skill runs the Python entry scripts in `E:\panda-oasis\UAssetAPI\scripts` to:
- Batch-parse `.uasset` files and report `OK/FAIL`
- Modify one property on a selected export
- Save to a new `.uasset` and verify the written result

Use this Skill for repeatable Unreal asset operations instead of ad-hoc manual command crafting.

## When to Use This Skill

Invoke this Skill when users ask to:
- Verify whether one or many `.uasset` files can be parsed
- Batch-check all `.uasset` files under a project folder
- Modify a property and save a new asset file
- Troubleshoot unknown export/property names during editing

Do not use this Skill for bulk structural refactors across many exports; use a dedicated custom tool for that.

## Prerequisites

Before executing commands:
1. Confirm `python` and `dotnet` are available.
2. Confirm repository root `E:\panda-oasis\UAssetAPI` exists.
3. Run commands from `E:\panda-oasis\UAssetAPI`.

## Core Workflow

1. **Readability check first**  
   Run batch parse to establish baseline parse health.
2. **Discover target export/property**  
   If names are unknown, run the edit script with a fake name to print hints.
3. **Modify and save to new file**  
   Write to a new output path, never overwrite source first.
4. **Verify output**  
   Re-open output and confirm script returns `EDIT_OK` plus expected before/after values.
5. **Report clearly**  
   Include exact file path, export, property, value type, and result.

## Commands

See `resources/commands.md` for command templates and examples.

## Notes

- Supported value types: `int`, `float`, `bool`, `string`, `name`
- For unknown engine versions, start with `UNKNOWN`
- For unversioned assets, pass explicit version (for example `VER_UE4_18`) if parsing fails
