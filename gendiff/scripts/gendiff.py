#!/usr/bin/env python3
"""Generate diff between two files."""

import argparse
import json


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
    
    # Читаем и парсим первый файл
    data1 = json.load(open(args.first_file))
    
    # Читаем и парсим второй файл
    data2 = json.load(open(args.second_file))
    
    # Выводим содержимое для проверки
    print("File 1 content:")
    print(data1)
    print("\nFile 2 content:")
    print(data2)


if __name__ == '__main__':
    main()
