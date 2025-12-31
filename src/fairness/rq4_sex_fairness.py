import os
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score

TARGET = "HeartDisease"

def generate_sex_fairness_table():
    os.makedirs("tables", exist_ok=True)

    df = pd.read_csv("data/processed/clean_data.csv")

    rf = joblib.load("models/random_forest.pkl")

    X = pd.get_dummies(df.drop(columns=[TARGET]), drop_first=True)
    y = df[TARGET]

    df["Prediction"] = rf.predict(X)

    results = []

    # Dynamically get sex groups (robust)
    for sex_value in df["Sex"].dropna().unique():
        subset = df[df["Sex"] == sex_value]

        # Safety check (important)
        if subset.empty:
            continue

        results.append({
            "Sex": str(sex_value),
            "Accuracy": accuracy_score(subset[TARGET], subset["Prediction"]),
            "F1_Score": f1_score(subset[TARGET], subset["Prediction"])
        })

    pd.DataFrame(results).to_excel(
        "tables/RQ4_Table_8_Performance_By_Sex.xlsx",
        index=False
    )

    print("RQ4 Table 8 generated successfully.")

if __name__ == "__main__":
    generate_sex_fairness_table()
