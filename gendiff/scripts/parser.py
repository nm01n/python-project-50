"""Parse configuration files."""

import json
import yaml


def parse(file_path):
    """Parse file based on extension.

    Args:
        file_path: Path to file

    Returns:
        Parsed data as dictionary
    """
    with open(file_path, 'r') as file:
        if file_path.endswith(('.yml', '.yaml')):
            return yaml.safe_load(file)
        elif file_path.endswith('.json'):
            return json.load(file)
        else:
            raise ValueError(f"Unsupported file format: {file_path}")
