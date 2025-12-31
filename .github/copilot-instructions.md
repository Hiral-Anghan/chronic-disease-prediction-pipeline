# GitHub Copilot / Agent instructions — chronic-disease-prediction-pipeline

Purpose: short, actionable guidance for an AI coding agent to be productive quickly in this repository.

## Big picture
- This is an end-to-end research pipeline implemented as an Apache Airflow project. The DAG `rq1_end_to_end_pipeline` (file: `dags/rq1_pipeline_dag.py`) runs four single-file tasks that execute Python scripts in `src/`:
  - `ingest_data` -> `src/data_ingestion/ingest_data.py`
  - `clean_data` -> `src/data_cleaning/clean_data.py`
  - `rq1_data_quality_analysis` -> `src/evaluation/rq1_data_quality_analysis.py`
  - `rq1_model_comparison` -> `src/modeling/rq1_model_comparison.py`
- The project is designed to run inside the official Airflow docker images (see `docker-compose.yaml`). Local development typically happens inside the running container where `/opt/airflow` is the working root.

## Key developer workflows
- Start and initialize the stack (creates DB and admin user):
  - docker compose up airflow-init
  - docker compose up -d
- Open Airflow UI at `http://localhost:8080` (default admin credentials created by the init container: username `admin`, password `admin`).
- Trigger the pipeline via UI or CLI (inside the webserver container):
  - docker compose exec airflow-webserver airflow dags trigger rq1_end_to_end_pipeline
- Run a single script interactively inside the webserver container (useful for fast iteration / debugging):
  - docker compose exec -it airflow-webserver bash
  - python /opt/airflow/src/data_cleaning/clean_data.py
- Logs are written to `logs/` (and to Airflow's UI); outputs are persisted to host folders via Docker volumes: `data/`, `figures/`, `tables/`.

## Project-specific conventions & patterns (important for code changes)
- Scripts in `src/` have `if __name__ == "__main__"` guards and print status on completion; follow the same pattern for new tasks.
- Two types of path patterns exist:
  - Container-rooted paths: e.g. `ingest_data.py` sets `base_dir = "/opt/airflow"` and writes to `/opt/airflow/data/...` (this assumes running inside the container). The DAG also calls scripts using `/opt/airflow/src/...`.
  - Relative paths: other scripts (cleaning, evaluation, modeling) read/write using relative paths such as `data/processed/raw_data.csv` and `tables/` — these work when run from the repository root or from within `/opt/airflow` in the container.
- Outputs and filenames are relied on by downstream steps — do not change names without updating the DAG and consumer scripts. Notable files:
  - `data/processed/raw_data.csv` (created by ingestion)
  - `data/processed/clean_data.csv` (created by cleaning)
  - `tables/RQ1_Table 1.xlsx` (data-quality report)
  - `tables/RQ1_Table_2_Model_Performance_Raw_vs_Clean.xlsx` (model comparison)
  - `figures/RQ1_Figure_1.pdf`, `RQ1_Figure_2.pdf`, `RQ1_Figure_4_model_Comparison.pdf`
- Modeling expectations:
  - Target column: `HeartDisease` — scripts raise explicit errors if the target is missing.
  - Categorical encoding is done via `pd.get_dummies(drop_first=True)`; numeric features are scaled with `StandardScaler` for Logistic Regression.
  - Random seeds (`random_state=42`) and `stratify=y` are used to make experiments reproducible.
- Dependencies: `requirements.txt` is empty. The project relies on packages used in scripts (pandas, numpy, matplotlib, seaborn, scikit-learn, openpyxl). In practice the Airflow image is used for execution; for local dev, ensure you `pip install` these packages in your environment.

## Integration & debugging tips
- If a task fails in Airflow, inspect the task logs from the UI (click into task instance) or check `logs/` on the host.
- To run or debug scripts exactly as the DAG does, run them from the container path used by the DAG. Example:
  - docker compose exec airflow-webserver python /opt/airflow/src/modeling/rq1_model_comparison.py
- Be careful with `ingest_data.py` which uses a hard-coded `/opt/airflow` base dir; running it on your host without adjustment may try to read `/opt/airflow/data/...` which doesn't exist. Options:
  - Run it inside the container (recommended); or
  - Modify the script to use an environment variable or a relative path (if you make this change, update the DAG call or add a fallback).
- Excel output requires `openpyxl` to write `.xlsx` files — make sure it's available in the runtime environment.

## Minimal checklist for contributing code
- Keep single-file scripts with clear CLI entrypoints (`if __name__ == '__main__'`), consistent logging/print messages, and stable output paths.
- If you change any filename or folder used by the DAG, update `dags/rq1_pipeline_dag.py` and any consumer scripts.
- Add a short note in `README.md` if you introduce a new developer workflow or dependency (e.g., `pip install <package>`).

## Short examples (copy-paste)
- Start stack & init (first time):
  - docker compose up airflow-init
  - docker compose up -d
- Trigger DAG from host shell:
  - docker compose exec airflow-webserver airflow dags trigger rq1_end_to_end_pipeline
- Run a script in container:
  - docker compose exec airflow-webserver python /opt/airflow/src/data_ingestion/ingest_data.py

---
If you'd like, I can open a PR with a small code fix to make `ingest_data.py` accept an env var fallback for `base_dir` (so scripts are easier to run both locally and in-container). Want me to implement that? 

If anything is missing or you'd like different emphasis in the instructions, tell me what to expand or adjust.