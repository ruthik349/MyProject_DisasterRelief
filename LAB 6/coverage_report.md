# LAB 6 — Coverage Report

| Suite | Tests | Result |
|---|---:|---|
| Functional/code coverage (`test_code_coverage.py`) | 11 | 11 passed |
| Branch coverage (`test_branch_coverage.py`) | 25 | 25 passed |

## Measured branch-suite coverage

Executed with `coverage run --branch -m pytest -q test_branch_coverage.py`.

| Target | Statements | Missed statements | Branches | Partial branches | Coverage |
|---|---:|---:|---:|---:|---:|
| `coffee_shop_order.py` | 63 | 0 | 44 | 0 | 100% |

All 44 measured branch outcomes were exercised. These figures apply to the source and branch test suite in this folder.

## Reproduce
```bash
python -m pip install -r requirements.txt
pytest -q test_code_coverage.py
coverage erase
coverage run --branch -m pytest -q test_branch_coverage.py
coverage report -m
```

Capture your own terminal screenshots if the course requires evidence from your personal machine.
