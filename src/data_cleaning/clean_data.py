import pandas as pd
import os

RAW_DATA_PATH = "/opt/airflow/data/processed/raw_data.csv"
CLEAN_DATA_PATH = "/opt/airflow/data/processed/clean_data.csv"


def clean_data():
    # Ensure output directory exists
    os.makedirs(os.path.dirname(CLEAN_DATA_PATH), exist_ok=True)

    # Load raw data
    df = pd.read_csv(RAW_DATA_PATH)

    # Example cleaning steps (adjust if needed)
    df = df.drop_duplicates()
    df = df.dropna()

    # Save cleaned data
    df.to_csv(CLEAN_DATA_PATH, index=False)

    print(f"Cleaned data saved to {CLEAN_DATA_PATH}")


if __name__ == "__main__":
    clean_data()
