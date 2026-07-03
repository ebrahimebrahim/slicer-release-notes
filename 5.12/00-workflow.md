# 5.12 Release Notes Workflow

This directory keeps the Slicer 5.12 release-note generation steps as numbered inputs and outputs.

## Inputs

- Slicer comparison: `v5.10.0..v5.12.0`
- Previous release tag date: `v5.10.0`, 2025-11-10
- Current release tag date: `v5.12.0`, 2026-06-23
- Initial extension catalog comparison: `/home/ebrahim/ExtensionsIndex`, `origin/5.10..origin/5.12`

The first automated extension catalog pass uses a branch comparison because the local ExtensionsIndex checkout contains post-5.12 changes on `main`. The later `06.3` curation pass corrects the "new extensions" list with a Slicer 5.10.0 release-date cutoff, because some extensions were added to both the `5.10` and `5.12` extension branches after the Slicer 5.10.0 release.

## Regeneration commands

Run from the Slicer source checkout:

```bash
bash 5.12-release-notes/scripts/01-generate-github-notes.sh \
  v5.12.0 \
  v5.10.0 \
  5.12-release-notes/01-github-generated.md

python3 5.12-release-notes/scripts/02-group-by-prefix.py \
  5.12-release-notes/01-github-generated.md \
  5.12-release-notes/02-grouped-by-prefix.md

python3 5.12-release-notes/scripts/03-normalize-grouped.py \
  5.12-release-notes/02-grouped-by-prefix.md \
  5.12-release-notes/03-grouped-normalized.md

python3 5.12-release-notes/scripts/04-collect-extension-changes.py \
  /home/ebrahim/ExtensionsIndex \
  origin/5.10 \
  origin/5.12 \
  5.12-release-notes/04-extension-changes.md

python3 5.12-release-notes/scripts/05-prepare-hackmd-draft.py \
  5.12-release-notes/05-curated-release-notes-draft.md \
  5.12-release-notes/06.0-curated-release-notes-hackmd.md
```

After making HackMD-oriented edits in a follow-up draft, extension logo placeholders can be replaced from extension repository metadata:

```bash
python3 5.12-release-notes/scripts/07-resolve-extension-icons.py \
  --notes 5.12-release-notes/06.1-curated-release-notes-hackmd.md \
  --output-map 5.12-release-notes/06.1.1-extension-icon-urls.json
```

The `06.3` draft switches extension additions from a branch-to-branch comparison to a Slicer 5.10.0 release-date cutoff. This includes extensions that were added to both the `5.10` and `5.12` extension branches after the 5.10.0 release, such as SimVascular:

```bash
python3 5.12-release-notes/scripts/07-resolve-extension-icons.py \
  --names ImpactReg ImpactSynth KonfAI RadReirradiation SEEGContactDetector SimVascular VoxTell \
  --output-map 5.12-release-notes/06.3.1-missing-extension-icon-urls.json
```

Extension descriptions can be added from each extension repository's `EXTENSION_DESCRIPTION` value in `CMakeLists.txt`:

```bash
python3 5.12-release-notes/scripts/08-add-extension-descriptions.py \
  --input 5.12-release-notes/06.3-curated-release-notes-hackmd-with-extension-fixes.md \
  --output 5.12-release-notes/06.4-curated-release-notes-hackmd-with-extension-descriptions.md \
  --output-map 5.12-release-notes/06.4.1-extension-descriptions.json
```

The `06.5` draft formats each active extension as a linked name followed by its description, preserving the existing category, tier, update, rename, and image sub-bullets:

```bash
python3 5.12-release-notes/scripts/09-inline-extension-descriptions.py \
  --input 5.12-release-notes/06.4-curated-release-notes-hackmd-with-extension-descriptions.md \
  --output 5.12-release-notes/06.5-curated-release-notes-hackmd-extension-inline-descriptions.md \
  --extension-index /home/ebrahim/ExtensionsIndex
```

The `06.6` draft is a manual cleanup pass over `06.5`. It removes GitHub-generated release-note boilerplate that is not used in Slicer release announcements, specifically the `New Contributors` section and the final `Full Changelog` link. It also moves the raw `Style` group from a top-level `### Style` section after Extensions to `#### Style` under `### Infrastructure`, where maintenance-only typo and spelling fixes fit better. This draft also adds a PW week slide link to the highlight figure placeholders.

The `06.7` draft is the community-edited final HackMD export. To migrate it to Discourse, run the heading-ID pass. This removes HackMD's `[TOC]` marker, converts Markdown headings to HTML headings with stable `heading--...` IDs, and inserts a static Markdown table of contents for the top-level content sections (`Summary`, `Highlights`, and `Changelog: 5.12.0`).

```bash
python3 5.12-release-notes/scripts/06-update-heading-ids-for-discourse.py \
  5.12-release-notes/06.7-curated-release-notes-hackmd-final.md \
  5.12-release-notes/07-curated-release-notes-discourse.md
```

If HackMD community edits continue after `06.7`, use the latest exported HackMD draft as the input to the Discourse heading-ID pass instead of the filename shown above.

## Files

- `01-github-generated.md`: Raw GitHub generated release notes.
- `02-grouped-by-prefix.md`: Raw notes grouped by commit prefix.
- `03-grouped-normalized.md`: Grouped notes with contributor handles removed and PR links normalized.
- `04-extension-changes.md`: Extension catalog changes from the 5.10 to 5.12 branches.
- `05-curated-release-notes-draft.md`: First editorial draft with summary, highlights, changelog, and placeholders.
- `06.0-curated-release-notes-hackmd.md`: Plain Markdown draft for HackMD community editing. It uses HackMD's dynamic `[TOC]` marker instead of explicit heading IDs.
- `06.1-curated-release-notes-hackmd.md`: User-edited HackMD draft with extension logo placeholders replaced.
- `06.1.1-extension-icon-urls.json`: Resolved extension icon paths and raw image URLs used during the `06.1` icon replacement pass.
- `06.2-curated-release-notes-hackmd-manual-edits.md`: User-edited HackMD draft with manual wording and logo removals.
- `06.3-curated-release-notes-hackmd-with-extension-fixes.md`: User-edited draft plus date-cutoff extension additions and corrected extension counts.
- `06.3.1-missing-extension-icon-urls.json`: Resolved icon URLs for the extensions added after switching to the release-date cutoff.
- `06.4-curated-release-notes-hackmd-with-extension-descriptions.md`: `06.3` plus extension descriptions extracted from `EXTENSION_DESCRIPTION`.
- `06.4.1-extension-descriptions.json`: Resolved descriptions and source `CMakeLists.txt` paths used for `06.4`.
- `06.5-curated-release-notes-hackmd-extension-inline-descriptions.md`: `06.4` with extension names linked to repositories and descriptions moved inline.
- `06.6-curated-release-notes-hackmd-a-few-manual-fixes.md`: `06.5` with GitHub-generated boilerplate removed, `Style` moved under Infrastructure, and an added PW week slide placeholder link.
- `06.7-curated-release-notes-hackmd-final.md`: Community-edited final HackMD draft.
- `07-curated-release-notes-discourse.md`: Discourse-ready publication artifact generated from `06.7`, with explicit heading IDs and a static section-level table of contents.
