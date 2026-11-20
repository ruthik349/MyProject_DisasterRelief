# LAB 4 — GitHub Copilot

## Disaster Relief Coordinator reference implementation
The `disaster-relief-code/` directory contains a dependency-light Node.js implementation of the Disaster Relief Supply & Volunteer Coordinator. Its README describes the routes, functional mapping and test command.

Run from the project subfolder:
```bash
cd disaster-relief-code
npm test
```

The 24 repository tests were rerun for this submission: 7 API tests and 17 logic tests passed when each file was executed directly with Node. The sandbox blocked the worker-based `npm test` wrapper with `spawn EPERM`; the exact commands and output are in [the terminal evidence file](../evidence/terminal-test-results.txt).

## Evidence still required
Add at least three genuine screenshots from your own GitHub Copilot Chat session showing prompts and Copilot replies. Add a short first-person note (2–3 lines) explaining what you changed and why. Do not use fabricated screenshots.

## Code location
The project code is included in this main repository under `disaster-relief-code/`. The files were originally already stored in the main repository's earlier Copilot folder.
