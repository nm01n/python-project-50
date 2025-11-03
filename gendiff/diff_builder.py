"""Build diff tree between two data structures."""


def build_diff(data1, data2):
    """Build diff tree between two dictionaries.

    Args:
        data1: First dictionary
        data2: Second dictionary

    Returns:
        List of diff nodes
    """
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in all_keys:
        if key not in data1:
            # Key only in second file - added
            diff.append({
                'key': key,
                'type': 'added',
                'value': data2[key]
            })
        elif key not in data2:
            # Key only in first file - removed
            diff.append({
                'key': key,
                'type': 'removed',
                'value': data1[key]
            })
        elif data1[key] == data2[key]:
            # Values are equal - unchanged
            diff.append({
                'key': key,
                'type': 'unchanged',
                'value': data1[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            # Both values are dicts - nested
            diff.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(data1[key], data2[key])
            })
        else:
            # Values are different - changed
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })

    return diff
