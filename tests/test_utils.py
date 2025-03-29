import pytest
from utilities.file_utils import read_json, write_json
from utilities.api_utils import fetch_data

def test_json_io(tmp_path):
    """Test JSON read/write"""
    test_file = tmp_path / "test.json"
    data = {"name": "Test", "value": 42}
    write_json(test_file, data)
    assert read_json(test_file) == data

def test_fetch_data():
    """Test API fetch"""
    data = fetch_data("https://jsonplaceholder.typicode.com/posts")
    assert isinstance(data, list)

if __name__ == "__main__":
    pytest.main()
