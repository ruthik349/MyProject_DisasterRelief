# LAB 7 — Hypothesis Fuzz Testing

**Assigned starter:** [SETAPESU26/L6_L7_03_coffee_shop_order](https://github.com/SETAPESU26/L6_L7_03_coffee_shop_order)

## Files
- `processor.py` — corrected drink-code, shot-price, and modifier parsing functions.
- `test_processor.py` — nine Hypothesis property-based tests.
- `requirements.txt` — Hypothesis and pytest dependencies.
- `fuzzing_report.md` — bug analysis and execution instructions.

## Defects fixed
1. Corrected the `MOc` menu-key typo to `MOC`.
2. Added type validation for drink-code input.
3. Added whitespace trimming and normalization for drink codes.
4. Replaced raw dictionary lookup failure with a clear `ValueError` for unknown codes.
5. Rejected missing/empty shot-price CSV input.
6. Converted malformed shot-price values into a consistent `ValueError`.
7. Rejected negative, NaN, and infinite prices.
8. Validated modifier syntax, empty keys/values, empty entries and duplicate keys; split only on the first colon.

## Run locally
```bash
python -m pip install -r requirements.txt
pytest -q
```

The nine Hypothesis tests are authored but were not run in the preparation environment because Hypothesis was unavailable and package downloads were blocked. The corrected functions passed 22 direct validation checks. Run the commands above before claiming the Hypothesis suite passed.
