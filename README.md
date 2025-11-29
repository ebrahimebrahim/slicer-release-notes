See https://github.com/Slicer/Slicer/wiki/Generating-Release-Notes

This repository tracks the automatic processing and manual curation steps involved in generating slicer release notes.

## TOC generation

To generate a TOC that works in a discourse post, the markdown headings need to be converted to html headings.
I use the script `convert_headings.py` to do this. Then I use md-toc on the original markdown to create the actual TOC, and then update the tags to match the html-converted ones.
For example:

```sh
python convert_headers.py changelog.md
uv tool install md-toc
md_toc github changelog.md | sed 's/(#/(#heading--/g' > toc.md
```
