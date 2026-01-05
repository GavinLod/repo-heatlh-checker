from pathlib import Path
from repo_checker.result import CheckResult

def check_required_files(repo_path : Path) -> list[CheckResult]:
    """ Verify that the repository contains a minimum set of baseline files
    
    Each rule returns machine-readable results that CI can act on"""

    required_files = ["README.md", "LICENSE", ".gitignore"]

    results: list[CheckResult] = []

    for filename in required_files:

        file_path = repo_path / filename

        if file_path.exists():
            results.append(
                CheckResult(
                    name = f"required_file:{filename}",
                    passed = True,
                    message = "Found",
                )
            )
        else: 
            results.append(
                CheckResult(
                    name=f"required_file:{filename}",
                    passed = False,
                    message = "Missing",
                )
            )
        
    return results

def check_github_actions_present(repo_path: Path) -> list[CheckResult]:
    """ Check that the repo has at least on GitHub Actions workflow"""

    workflows_dir = repo_path / ".github" / "workflows"

    if not workflows_dir.exists():
        return [
            CheckResult(
                name = "ci:github_actions",
                passed = False,
                message = "Missing .github/workflows directory",

            )
        ]
    workflow_files = list(workflows_dir.glob("*.yml")) + list(workflows_dir.glob("*.yaml"))
    passed = len(workflow_files) > 0

    return [
        CheckResult(
            name = "ci:github_actions",
            passed=passed,
            message="Found workflow(s)" if passed else "No workflow files found",


        )
    ]
