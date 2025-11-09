"""Tests for gendiff module."""

from gendiff import generate_diff
import os


def get_fixture_path(filename):
    """Get path to fixture file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', filename)


def read_file(filepath):
    """Read file content."""
    with open(filepath, 'r') as f:
        return f.read().strip()


def test_generate_diff_json_flat():
    """Test diff generation for flat JSON files."""
    file1_path = get_fixture_path('file1.json')
    file2_path = get_fixture_path('file2.json')
    expected = read_file(get_fixture_path('expected_result.txt'))

    result = generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.json')

    assert result == expected


def test_generate_diff_yaml_flat():
    """Test diff generation for flat YAML files."""
    file1_path = get_fixture_path('file1.yml')
    file2_path = get_fixture_path('file2.yml')
    expected = read_file(get_fixture_path('expected_result.txt'))

    result = generate_diff(file1_path, file2_path)

    assert result == expected


def test_generate_diff_json_nested():
    """Test diff generation for nested JSON files."""
    file1_path = get_fixture_path('file1_nested.json')
    file2_path = get_fixture_path('file2_nested.json')
    expected = read_file(get_fixture_path('expected_nested.txt'))

    result = generate_diff(file1_path, file2_path)

    assert result == expected


def test_generate_diff_yaml_nested():
    """Test diff generation for nested YAML files."""
    file1_path = get_fixture_path('file1_nested.yml')
    file2_path = get_fixture_path('file2_nested.yml')
    expected = read_file(get_fixture_path('expected_nested.txt'))

    result = generate_diff(file1_path, file2_path)

    assert result == expected


def test_generate_diff_plain_format():
    """Test diff generation in plain format."""
    file1_path = get_fixture_path('file1_nested.json')
    file2_path = get_fixture_path('file2_nested.json')
    expected = read_file(get_fixture_path('expected_nested_plain.txt'))

    result = generate_diff(file1_path, file2_path, 'plain')

    assert result == expected


def test_generate_diff_json_format():
    """Test diff generation in JSON format."""
    file1_path = get_fixture_path('file1_nested.json')
    file2_path = get_fixture_path('file2_nested.json')
    expected = read_file(get_fixture_path('expected_nested_json.txt'))

    result = generate_diff(file1_path, file2_path, 'json')

    assert result == expected
