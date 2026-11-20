# LAB 7 — Hypothesis Fuzzing Report

## Objective
Use property-based tests to exercise `lookup_drink_code`, `calculate_average_shot_cost`, and `parse_order_modifiers` with generated valid and arbitrary malformed input.

## Bugs identified and fixes

| # | Defect in starter | Correction |
|---:|---|---|
| 1 | Mocha key was `MOc`, but input is uppercased | Corrected to `MOC` |
| 2 | Non-string drink codes caused an attribute error | Validate type and raise `ValueError` |
| 3 | Leading/trailing spaces were not normalized | Strip whitespace |
| 4 | Unknown codes leaked a dictionary `KeyError` | Raise a descriptive `ValueError` |
| 5 | Empty shot-price CSV caused division by zero | Reject empty input |
| 6 | Non-numeric values leaked conversion exceptions | Normalize to `ValueError` |
| 7 | Negative, NaN and infinite prices were accepted | Reject non-finite and negative prices |
| 8 | Modifier parser crashed on malformed pairs and silently overwrote duplicate keys | Validate syntax, split once at first colon, reject empty/duplicate keys |

## Property-based test design
Nine Hypothesis tests cover arbitrary text, `None`, supported codes and casing, generated numeric price lists, malformed numeric CSVs, arbitrary modifier strings, generated valid key/value mappings, and malformed/duplicate modifiers.

## Execution status
The corrected functions passed 22 direct validation checks during preparation. The environment did not have Hypothesis installed and could not access package downloads, so the nine Hypothesis tests were authored but not executed here. Install with `python -m pip install -r requirements.txt`, then run `pytest -q`. No Hypothesis pass count is claimed.
