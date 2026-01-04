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