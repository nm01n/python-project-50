"""Tests for gendiff module."""

from gendiff import generate_diff
import os


def get_fixture_path(filename):
    """Get path to fixture file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', filename)


def read_file(filepath):
    """Read file content."""
    with open(filepath, 'r') as f:
        return f.read().strip()  # Добавили .strip()


def test_generate_diff_json():
    """Test diff generation for JSON files."""
    file1_path = get_fixture_path('file1.json')
    file2_path = get_fixture_path('file2.json')
    expected = read_file(get_fixture_path('expected_result.txt'))
    
    result = generate_diff(file1_path, file2_path)
    
    assert result == expected
