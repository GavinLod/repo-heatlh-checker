import argparse
from pathlib import Path
from repo_checker.runner import run_all_checks

def main() -> None:
    parser = argparse.ArgumentParser(description = "Check repository health")
    parser.add_argument("path", nargs="?", default=".", help="Path to repository (default: current directory)")
    args = parser.parse_args()

    repo_path = Path(args.path).resolve()
    results = run_all_checks(repo_path)

    failed = [r for r in results if not r.passed]
    #Print detailed results
    for r in results: 
        status = "PASS" if r.passed else "FAIL"
        print(f"[{status}] {r.name}: {r.message}")

    #Print summary
    print()
    print(f"Summary: {len(results) - len(failed)}/{len(results)} checks passed")

    #Exit code for CI
    raise SystemExit(1 if failed else 0)

if __name__ == "__main__":
    main()
    