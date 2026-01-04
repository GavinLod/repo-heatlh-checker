from pathlib import Path
from repo_checker.checks import check_required_files

def test_check_required_files(tmp_path: Path):
    
    (tmp_path / "README.md").touch()
    (tmp_path / "LICENSE").touch()

    results = check_required_files(tmp_path)

    result_map = {r.name: r.passed for r in results}

    assert result_map["required_file:README.md"] is True
    assert result_map["required_file:LICENSE"] is True
    assert result_map["required_file:.gitignore"] is False