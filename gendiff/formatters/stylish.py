"""Stylish formatter for diff output."""


def format_stylish(diff, depth=0):
    """Format diff tree in stylish format.

    Args:
        diff: Diff tree
        depth: Current nesting depth

    Returns:
        Formatted string
    """
    indent = ' ' * (depth * 4)
    bracket_indent = ' ' * (depth * 4)
    lines = ['{']

    for node in diff:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            children_str = format_stylish(node['children'], depth + 1)
            lines.append(f'{indent}    {key}: {children_str}')
        elif node_type == 'unchanged':
            value_str = stringify(node['value'], depth + 1)
            lines.append(f'{indent}    {key}: {value_str}')
        elif node_type == 'removed':
            value_str = stringify(node['value'], depth + 1)
            lines.append(f'{indent}  - {key}: {value_str}')
        elif node_type == 'added':
            value_str = stringify(node['value'], depth + 1)
            lines.append(f'{indent}  + {key}: {value_str}')
        elif node_type == 'changed':
            old_value_str = stringify(node['old_value'], depth + 1)
            new_value_str = stringify(node['new_value'], depth + 1)
            lines.append(f'{indent}  - {key}: {old_value_str}')
            lines.append(f'{indent}  + {key}: {new_value_str}')

    lines.append(f'{bracket_indent}}}')
    return '\n'.join(lines)


def stringify(value, depth):
    """Convert value to string representation.

    Args:
        value: Value to stringify
        depth: Current depth for formatting dicts

    Returns:
        String representation
    """
    if isinstance(value, dict):
        return dict_to_string(value, depth)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if value == '':
        return ''
    return str(value)


def dict_to_string(data, depth):
    """Convert dictionary to formatted string.

    Args:
        data: Dictionary to convert
        depth: Current depth

    Returns:
        Formatted string
    """
    indent = ' ' * (depth * 4)
    lines = ['{']

    for key, value in data.items():
        value_str = stringify(value, depth + 1)
        lines.append(f'{indent}    {key}: {value_str}')

    lines.append(f'{indent}}}')
    return '\n'.join(lines)
