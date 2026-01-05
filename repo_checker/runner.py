from pathlib import Path
from repo_checker.result import CheckResult
from repo_checker.checks import check_required_files, check_github_actions_present

def run_all_checks(repo_path: Path) -> list[CheckResult]:
    """ Runs every check and returns a flat list of results"""
    results: list[CheckResult] = []
    results.extend(check_required_files(repo_path))
    results.extend(check_github_actions_present(repo_path))
    return results 