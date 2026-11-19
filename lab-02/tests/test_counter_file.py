import pytest
import app


@pytest.fixture
def counter_file(tmp_path, monkeypatch):
    path = tmp_path / "dir" / "bump_file.txt"
    monkeypatch.setattr(app, "COUNTER_FILE", path)
    return path


def test_creates_file_and_parent_dir(counter_file):
    assert not counter_file.exists()
    assert not counter_file.parent.exists()
    
    app.bump_file()
    
    assert counter_file.parent.is_dir()
    assert counter_file.is_file()
    
    
def test_starts_from_zero_when_file_missing(counter_file):
    assert app.bump_file() == 1
    assert counter_file.read_text() == "1"