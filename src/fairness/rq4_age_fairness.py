import os
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score

TARGET = "HeartDisease"

def add_age_groups(df):
    df = df.copy()
    df["AgeGroup"] = pd.cut(
        df["Age"],
        bins=[0, 45, 60, 120],
        labels=["Young (<45)", "Middle (45–60)", "Older (>60)"]
    )
    return df

def generate_age_fairness_table():
    os.makedirs("tables", exist_ok=True)

    df = pd.read_csv("data/processed/clean_data.csv")

    rf = joblib.load("models/random_forest.pkl")

    X = pd.get_dummies(df.drop(columns=[TARGET]), drop_first=True)
    y = df[TARGET]

    df["Prediction"] = rf.predict(X)
    df = add_age_groups(df)

    results = []

    for group in df["AgeGroup"].dropna().unique():
        subset = df[df["AgeGroup"] == group]

        if subset.empty:
            continue

        results.append({
            "AgeGroup": str(group),
            "Accuracy": accuracy_score(subset[TARGET], subset["Prediction"]),
            "F1_Score": f1_score(subset[TARGET], subset["Prediction"])
        })

    pd.DataFrame(results).to_excel(
        "tables/RQ4_Table_9_Performance_By_Age_Group.xlsx",
        index=False
    )

    print("RQ4 Table 9 generated successfully.")

if __name__ == "__main__":
    generate_age_fairness_table()
