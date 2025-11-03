"""Plain formatter for diff output."""


def format_plain(diff, path=''):
    """Format diff tree in plain format.

    Args:
        diff: Diff tree
        path: Current property path

    Returns:
        Formatted string
    """
    lines = []

    for node in diff:
        key = node['key']
        node_type = node['type']
        current_path = f"{path}.{key}" if path else key

        if node_type == 'nested':
            lines.append(format_plain(node['children'], current_path))
        elif node_type == 'added':
            value_str = stringify_value(node['value'])
            lines.append(
                f"Property '{current_path}' was added with value: {value_str}"
            )
        elif node_type == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif node_type == 'changed':
            old_value_str = stringify_value(node['old_value'])
            new_value_str = stringify_value(node['new_value'])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_value_str} to {new_value_str}"
            )
        # unchanged nodes are skipped in plain format

    return '\n'.join(filter(None, lines))


def stringify_value(value):
    """Convert value to string representation for plain format.

    Args:
        value: Value to stringify

    Returns:
        String representation
    """
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
