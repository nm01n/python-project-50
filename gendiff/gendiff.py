"""Generate diff between two data structures."""

from gendiff.parser import parse
from gendiff.diff_builder import build_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """Generate diff between two configuration files.

    Args:
        file_path1: Path to first file
        file_path2: Path to second file
        format_name: Output format (default: stylish)

    Returns:
        String with formatted diff
    """
    data1 = parse(file_path1)
    data2 = parse(file_path2)

    diff_tree = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff_tree)
    elif format_name == 'plain':
        return format_plain(diff_tree)
    else:
        raise ValueError(f"Unknown format: {format_name}")
