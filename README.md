# Financial Data Analysis 1

Homework and coursework notebooks for CMU's Financial Data Analysis I.

## Setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m ipykernel install --user --name=financial_data_analysis_1 --display-name="Financial Data Analysis 1"
```

Open this folder in VS Code, open any notebook under `notebooks/`, and select the
**"Financial Data Analysis 1"** kernel (top-right of the notebook) — that's the
`.venv` above, registered so it shows up by name in the kernel picker.

## Structure

- `notebooks/` — one notebook per homework/topic (e.g. `hw1.ipynb`)
- `data/` — local datasets, gitignored (not committed — keep the repo light)
- `requirements.txt` — pinned package versions (`pip freeze` output)

## Course materials

Syllabus, lecture PDFs, and homework prompts live outside this repo at
`..\Financial Data Analysis I\` (not versioned — just reference material).
