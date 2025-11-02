"""Generate diff between two data structures."""

import json


def generate_diff(file_path1, file_path2):
    """Generate diff between two JSON files.
    
    Args:
        file_path1: Path to first file
        file_path2: Path to second file
    
    Returns:
        String with formatted diff
    """
    # Читаем и парсим файлы
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    
    # Получаем все уникальные ключи из обоих файлов
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    
    # Строим список строк дифа
    diff_lines = ['{']
    
    for key in all_keys:
        # Ключ есть в обоих файлах
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                # Значения одинаковые
                diff_lines.append(f'    {key}: {format_value(data1[key])}')
            else:
                # Значения разные - сначала из первого файла, потом из второго
                diff_lines.append(f'  - {key}: {format_value(data1[key])}')
                diff_lines.append(f'  + {key}: {format_value(data2[key])}')
        elif key in data1:
            # Ключ только в первом файле
            diff_lines.append(f'  - {key}: {format_value(data1[key])}')
        else:
            # Ключ только во втором файле
            diff_lines.append(f'  + {key}: {format_value(data2[key])}')
    
    diff_lines.append('}')
    
    return '\n'.join(diff_lines)


def format_value(value):
    """Format value for output.
    
    Args:
        value: Any value
    
    Returns:
        Formatted string
    """
    if isinstance(value, bool):
        return str(value).lower()
    return value
