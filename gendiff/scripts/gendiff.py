#!/usr/bin/env python3
"""Generate diff between two files."""

import argparse


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
    
    # Пока просто выводим информацию
    print(f"First file: {args.first_file}")
    print(f"Second file: {args.second_file}")
    if args.format:
        print(f"Format: {args.format}")


if __name__ == '__main__':
    main()
