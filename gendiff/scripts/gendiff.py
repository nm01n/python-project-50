#!/usr/bin/env python3
"""Generate diff between two files."""

import argparse
from gendiff import generate_diff


def main():
    """Run gendiff CLI."""
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output'
    )
    
    args = parser.parse_args()
    
    # Генерируем и выводим diff
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
