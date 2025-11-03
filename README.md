### Hexlet tests and linter status:
[![Actions Status](https://github.com/nm01n/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/nm01n/python-project-50/actions)
[![Python CI](https://github.com/nm01n/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/nm01n/python-project-50/actions/workflows/main.yml)

# Difference Calculator

A tool for finding differences between two data structures.

Supports JSON and YAML formats with multiple output formats.

## Installation
```bash
uv tool install .
```

## Usage

### As CLI tool
```bash
# Default stylish format
gendiff file1.json file2.json

# Plain format
gendiff --format plain file1.json file2.json

# JSON format
gendiff --format json file1.json file2.json

# With YAML files
gendiff file1.yml file2.yml
```

### As library
```python
from gendiff import generate_diff

# Stylish format (default)
diff = generate_diff('file1.json', 'file2.json')
print(diff)

# Plain format
diff = generate_diff('file1.json', 'file2.json', 'plain')
print(diff)

# JSON format
diff = generate_diff('file1.json', 'file2.json', 'json')
print(diff)
```

## Supported Formats

### Input formats:
- JSON (`.json`)
- YAML (`.yml`, `.yaml`)

### Output formats:
- **stylish** (default) - tree-like format with indentation
- **plain** - flat text format describing changes
- **json** - JSON format for programmatic use

## Demo

[![asciicast](https://asciinema.org/a/3si9K5kexRm1COOtg4n4Azl8G.svg)](https://asciinema.org/a/3si9K5kexRm1COOtg4n4Azl8G)
