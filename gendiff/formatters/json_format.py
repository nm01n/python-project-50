"""JSON formatter for diff output."""

import json


def format_json(diff):
    """Format diff tree in JSON format.

    Args:
        diff: Diff tree

    Returns:
        JSON string
    """
    return json.dumps(diff, indent=2)
