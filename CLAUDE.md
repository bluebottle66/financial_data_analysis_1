# Financial Data Analysis 1

CMU coursework project — homework notebooks, mostly regression/time-series
work on financial data (see the `MeanModels`/`SimpleLinearReg` lecture PDFs
in `..\Financial Data Analysis I\` for the syllabus context).

## Environment

- Python venv at `.venv/`, kernel registered as **"Financial Data Analysis 1"**
  (`financial_data_analysis_1` kernelspec).
- Installed: jupyter, ipykernel, pandas, numpy, matplotlib, seaborn, scipy,
  statsmodels, scikit-learn, openpyxl. `requirements.txt` is a `pip freeze`
  snapshot — reinstall with `pip install -r requirements.txt`.

## Conventions

- One notebook per homework/topic under `notebooks/` (e.g. `hw1.ipynb`).
- Raw datasets go in `data/` — gitignored, not committed (keep the repo to
  code/notebooks, not coursework data files).
- Local git only, no remote — this is coursework, not shared infrastructure.
