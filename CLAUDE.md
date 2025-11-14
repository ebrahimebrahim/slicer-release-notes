# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository tracks the automatic processing and manual curation steps involved in generating 3D Slicer release notes. The workflow combines GitHub's automated release notes generation with scripted preprocessing and manual organization.

## Repository Structure

### Generated Files (per release)

- **`slicer-X.Y-notes.md`** - Raw GitHub-generated release notes (bullet list of all PRs)
- **`slicer-X.Y-grouped-notes.md`** - Preprocessed notes grouped by commit type (ENH, BUG, DOC, etc.)
- **`slicer-X.Y-pr-summaries.md`** - Human-written summaries for significant PRs (manual curation)
- **`tmp-helpers/slicer-X.Y-feature-summaries.md`** - Summaries organized by feature category (manual curation)

### Scripts

- **`preprocess.sh`** - Groups release notes by conventional commit prefixes

### Commit Message Prefixes

Slicer uses standard commit prefixes that the preprocessing groups by:
- `ENH:` - Improvements (new features, enhancements)
- `PERF:` - Performance improvements
- `BUG:` - Fixes
- `DOC:` - Documentation changes
- `COMP:` - Compilation/build changes
- `STYLE:` - Style changes (no logic impact)

The script also separates entries by contributor type:
- Regular contributors
- Bot-generated entries (@slicerbot, @dependabot, @slicer-app)
- Uncategorized entries (missing prefix)

## Workflow

The complete workflow for generating Slicer release notes is documented at:
https://github.com/Slicer/Slicer/wiki/Generating-Release-Notes

### High-Level Steps

1. **Generate base notes from GitHub**
   - Use GitHub's "Generate release notes" feature for a tag
   - Specify previous tag as reference point
   - Save to `slicer-X.Y-notes.md`

2. **Preprocess and group**
   ```bash
   export SLICER_RELEASE_NOTES="slicer-X.Y-notes.md"
   export SLICER_RELEASE_NOTES_GROUPED="slicer-X.Y-grouped-notes.md"
   ./preprocess.sh
   ```
   This uses `ack` and `sed` to organize entries by type.

3. **Manual curation**
   - Review grouped notes
   - Write human-readable summaries for important PRs
   - Organize features into user-facing categories
   - Separate "Actual features" from "Groundwork" and "Internal improvements"

4. **Collaborative review**
   - Share with core developers via HackMD or similar
   - Iterate on categorization and wording

5. **Publish to Discourse**
   - Post structured release notes to https://discourse.slicer.org/
   - Use proper markdown headings for navigation

## File Naming Convention

Files follow the pattern: `slicer-<major>.<minor>-<type>.md`

Examples:
- `slicer-5.10-notes.md`
- `slicer-5.10-grouped-notes.md`
- `slicer-5.10-pr-summaries.md`

## Preprocessing Script Details

The `preprocess.sh` script:
1. Reads from `$SLICER_RELEASE_NOTES` (input file)
2. Writes to `$SLICER_RELEASE_NOTES_GROUPED` (output file)
3. Uses `ack` to filter entries by prefix patterns
4. Uses `sed` to clean up formatting (removes prefix from grouped entries)
5. Excludes bot contributions from main categories
6. Creates sections for: Improvements, Performance, Fixes, Documentation, Compilation, Style, Uncategorized, and separate bot sections

### Dependencies
- `ack` - Pattern searching tool
- `sed` - Stream editor for text transformations
- Standard bash shell

## Manual Curation Strategy

When writing summaries for PRs:

### Feature Categories (for major/minor releases)
- **Actual Features** - User-visible functionality
- **Groundwork for Future Features** - Infrastructure enabling future work
- **Visual Prettiness** - UI/UX improvements
- **Updates** - Dependency version bumps
- **Extension Config** - Extension system improvements
- **Internal Code Improvements** - API enhancements, refactoring, logging

### Writing Style
- Focus on user impact, not implementation details
- Explain what users can now do, not how code changed
- Keep summaries 1-2 sentences
- Link to PR with format: `([PR-XXXX](https://github.com/Slicer/Slicer/pull/XXXX))`

### Example
Bad: "Refactored vtkMRMLSliceLogic::UpdatePipeline to use Nth Layer API"
Good: "Lays groundwork for supporting unlimited number of overlays in slice views"

## Version Control

This repository is a git repository tracking the evolution of release notes through the curation process. Each transformation step (preprocessing, grouping, summarizing, reorganizing) should be committed separately to maintain history.

Typical commit sequence:
1. "Add GitHub-generated release notes"
2. "Pre-process and group release notes"
3. "Remove contributor handles from grouped notes"
4. "Normalize PR references"
5. ...

## Context: Parent Repository

This repository lives within the main Slicer source tree at `Slicer/slicer-release-notes/` but is a separate git repository tracking release notes for https://github.com/Slicer/Slicer.
