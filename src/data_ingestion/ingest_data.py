import os
import pandas as pd

def ingest_data():
    base_dir = "/opt/airflow"
    input_path = os.path.join(base_dir, "data", "sample", "heart_disease.csv")
    output_dir = os.path.join(base_dir, "data", "processed")
    output_path = os.path.join(output_dir, "raw_data.csv")

    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(input_path)

    if df.empty:
        raise ValueError("Ingested dataset is empty.")

    df.to_csv(output_path, index=False)
    print(f"Data ingestion completed. Rows: {len(df)}, Columns: {len(df.columns)}")

if __name__ == "__main__":
    ingest_data()
