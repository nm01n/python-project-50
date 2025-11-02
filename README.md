### Hexlet tests and linter status:
[![Actions Status](https://github.com/nm01n/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/nm01n/python-project-50/actions)

# Difference Calculator

A tool for finding differences between two data structures.

## Installation
```bash
uv tool install .
```

## Usage

### As CLI tool
```bash
gendiff file1.json file2.json
```

### As library
```python
from gendiff import generate_diff

diff = generate_diff('file1.json', 'file2.json')
print(diff)
```

## Demo

[![asciicast](https://asciinema.org/a/m8AsbXcTgQ7AHet05yevo0E6T.svg)](https://asciinema.org/a/m8AsbXcTgQ7AHet05yevo0E6T)
