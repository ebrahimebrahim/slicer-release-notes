#!/usr/bin/env python3
"""
Convert markdown headers to HTML headers with id attributes.

(This script is AI generated)

Example:
    ### Documentation -> <h3 id="heading--documentation">Documentation</h3>
"""

import re
import sys
from pathlib import Path


def slugify(text: str) -> str:
    """Convert header text to a URL-friendly slug."""
    # Convert to lowercase
    slug = text.lower()
    # Replace spaces and special chars with hyphens
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    return slug


def convert_header(match: re.Match) -> str:
    """Convert a markdown header match to an HTML header."""
    hashes = match.group(1)
    header_text = match.group(2).strip()

    # Determine header level (number of # symbols)
    level = len(hashes)

    # Create the slug for the id attribute
    slug = slugify(header_text)

    return f'<h{level} id="heading--{slug}">{header_text}</h{level}>'


def convert_markdown_headers(content: str) -> str:
    """Convert all markdown headers in content to HTML headers."""
    # Match markdown headers: one or more # at start of line, followed by space and text
    pattern = r'^(#{1,6})\s+(.+)$'
    return re.sub(pattern, convert_header, content, flags=re.MULTILINE)


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_headers.py <input_file> [output_file]")
        print("If output_file is not specified, will append '_converted' to input filename.")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)

    # Determine output path
    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.with_stem(input_path.stem + '_converted')

    # Read input file
    content = input_path.read_text(encoding='utf-8')

    # Convert headers
    converted = convert_markdown_headers(content)

    # Write output file
    output_path.write_text(converted, encoding='utf-8')

    print(f"Converted: {input_path} -> {output_path}")


if __name__ == '__main__':
    main()
