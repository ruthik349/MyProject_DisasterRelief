# LAB 6 — Code and Branch Coverage

**Assigned starter:** [SETAPESU26/L6_L7_03_coffee_shop_order](https://github.com/SETAPESU26/L6_L7_03_coffee_shop_order)

## Files
- `coffee_shop_order.py` — coffee-shop batch and espresso-temperature logic, with validation for malformed orders and customizations.
- `test_code_coverage.py` — 11 functional tests.
- `test_branch_coverage.py` — 25 tests targeting all conditional outcomes.
- `requirements.txt` — test dependencies.
- `coverage_report.md` and `coverage_evidence.pdf` — measured test and coverage results.

## Run locally
```bash
python -m pip install -r requirements.txt
pytest -q test_code_coverage.py
coverage erase
coverage run --branch -m pytest -q test_branch_coverage.py
coverage report -m
```

## Verified result in the build environment
- Functional/code-coverage suite: **11 passed**.
- Branch-coverage suite: **25 passed**.
- `coffee_shop_order.py`: **100% statement coverage and 44/44 branch outcomes** under the 25-test branch suite.
