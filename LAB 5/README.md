# LAB 5 — Static Code Analysis

**Project:** Energy Consumption & Tariff Calculator

## Included files
- `energy_system.py` — corrected Python source copied from [L5_03_energy_tariff](https://github.com/ruthik349/L5_03_energy_tariff).
- `issue_table_and_reflections.md` — issue table and reflection answers from that repository.
- `reports/` — two Lab 5 PDF documents found in your separate repositories.

## Source repositories
- [L5_03_energy_tariff](https://github.com/ruthik349/L5_03_energy_tariff)
- [SE-DEMO](https://github.com/ruthik349/SE-DEMO)

## Reproduce the analysis
```bash
pip install pylint bandit flake8
python energy_system.py
pylint energy_system.py
bandit -r energy_system.py
flake8 energy_system.py
```

The handoff reports Pylint 6.14 → 9.76, Bandit 1 Medium → 0, and Flake8 12 → 0. These are reported values; rerun the commands locally if your instructor requires fresh terminal evidence. The two PDFs are preserved under different filenames because they came from separate source repositories.
