# LAB 5 — Static Code Analysis

**Project:** Energy Consumption & Tariff Calculator  
**Source repository:** [ruthik349/L5_03_energy_tariff](https://github.com/ruthik349/L5_03_energy_tariff)  
**Additional submission material:** [ruthik349/SE-DEMO](https://github.com/ruthik349/SE-DEMO)

The `energy_system.py` source, issue table, reflection and available before/after reports are retained here. The source report in the original repository includes a Lab 5 PDF; SE-DEMO also contains a separate Lab 5 PDF. Review both and retain the version required by the course handout.

To reproduce analysis locally:
```bash
pip install pylint bandit flake8
python energy_system.py
pylint energy_system.py
bandit -r energy_system.py
flake8 energy_system.py
```

Reported results from the handoff: Pylint 6.14 → 9.76, Bandit 1 Medium → 0, Flake8 12 → 0. Treat these as reported results until independently reproduced on the submission machine.
