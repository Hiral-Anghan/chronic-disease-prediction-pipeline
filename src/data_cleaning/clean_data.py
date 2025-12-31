# this code will read raw dataset 
# and clean data and saved in the proceed folder with name clean_data
# data cleaning
# Drop duplicate rows
# Fill missing numerical values with median
# Fill missing categorical values with mode
# Cap outliers using IQR (for cholesterol, blood pressure, etc.)

import os
import pandas as pd
import numpy as np


def clean_data():
    # Define paths (relative & reproducible)
    input_path = os.path.join("data", "processed", "raw_data.csv")
    output_dir = os.path.join("data", "processed")
    output_path = os.path.join(output_dir, "clean_data.csv")

    # Load raw data
    df = pd.read_csv(input_path)
 
    if df.empty:
        raise ValueError("Raw data is empty. Cleaning aborted.")

    # 1. Remove duplicates
    df = df.drop_duplicates()

    # 2. Handle missing values
    for col in df.columns:
        if df[col].dtype in ["int64", "float64"]:
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

    # 3. Handle outliers using IQR (numerical columns only)
    numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in numerical_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        df[col] = np.clip(df[col], lower_bound, upper_bound)

    # Save cleaned dataset
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(
        f"Data cleaning completed. Rows: {len(df)}, Columns: {len(df.columns)}"
    )


if __name__ == "__main__":
    clean_data()