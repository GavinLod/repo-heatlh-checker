from pathlib import Path
from repo_checker.checks import check_required_files, check_github_actions_present


def test_check_required_files(tmp_path: Path):
    (tmp_path / "README.md").touch()
    (tmp_path / "LICENSE").touch()
    #Intentionally missing .gitignore

    results = check_required_files(tmp_path)
    result_map = {r.name: r.passed for r in results}

    assert result_map["required_file:README.md"] is True
    assert result_map["required_file:LICENSE"] is True
    assert result_map["required_file:.gitignore"] is False


def test_check_github_actions_present_missing_directory(tmp_path: Path):
    results = check_github_actions_present(tmp_path)
    assert len(results) == 1
    assert results[0].passed is False
    assert results[0].name == "ci:github_actions"


def test_check_github_actions_present_with_workflow(tmp_path: Path):
    workflows = tmp_path / ".github" / "workflows"
    workflows.mkdir(parents=True)

    (workflows / "ci.yml").write_text("name: CI\non: [push]\njobs: {}\n")

    results = check_github_actions_present(tmp_path)
    assert len(results) == 1
    assert results[0].passed is True
