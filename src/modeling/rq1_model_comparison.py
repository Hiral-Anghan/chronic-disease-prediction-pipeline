'''
################################
You want ONE single script that:

Loads RAW data

Trains:

Logistic Regression

Random Forest
→ before cleaning

Loads CLEAN data

Trains:

Logistic Regression

Random Forest
→ after cleaning

Compares results

Creates ONE comparison table
👉 RQ1 Table 2: Model performance before vs after cleaning
################################

'''


import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import matplotlib.pyplot as plt

TARGET_COL = "HeartDisease"


def train_models(df, data_version):
    """
    Train Logistic Regression and Random Forest
    Returns performance metrics as a DataFrame
    """

    X = df.drop(columns=[TARGET_COL])
    y = df[TARGET_COL]

    # Encode categorical variables
    X = pd.get_dummies(X, drop_first=True)

    # Minimal imputation (needed for RAW & CLEAN safety)
    for col in X.columns:
        if X[col].dtype in ["int64", "float64"]:
            X[col].fillna(X[col].median(), inplace=True)
        else:
            X[col].fillna(X[col].mode()[0], inplace=True)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    results = []

    # ---------------- Logistic Regression ----------------
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    lr = LogisticRegression(max_iter=1000, random_state=42)
    lr.fit(X_train_scaled, y_train)
    lr_preds = lr.predict(X_test_scaled)

    results.append({
        "Model": "Logistic Regression",
        "Data_Version": data_version,
        "Accuracy": accuracy_score(y_test, lr_preds),
        "F1_Score": f1_score(y_test, lr_preds)
    })

    # ---------------- Random Forest ----------------
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    rf_preds = rf.predict(X_test)

    results.append({
        "Model": "Random Forest",
        "Data_Version": data_version,
        "Accuracy": accuracy_score(y_test, rf_preds),
        "F1_Score": f1_score(y_test, rf_preds)
    })

    return pd.DataFrame(results)


def rq1_full_comparison():
    # ---------------- Paths ----------------
    raw_path = os.path.join("data", "processed", "raw_data.csv")
    clean_path = os.path.join("data", "processed", "clean_data.csv")
    output_dir = "tables"

    os.makedirs(output_dir, exist_ok=True)

    # ---------------- Load datasets ----------------
    raw_df = pd.read_csv(raw_path)
    clean_df = pd.read_csv(clean_path)

    if TARGET_COL not in raw_df.columns:
        raise ValueError("Target column missing in raw data.")

    if TARGET_COL not in clean_df.columns:
        raise ValueError("Target column missing in clean data.")

    # ---------------- Train models ----------------
    raw_results = train_models(raw_df, "Raw")
    clean_results = train_models(clean_df, "Clean")

    # ---------------- Combine & save ----------------
    final_results = pd.concat([raw_results, clean_results], ignore_index=True)

    output_path = os.path.join(
        output_dir,
        "RQ1_Table_2_Model_Performance_Raw_vs_Clean.xlsx"
    )

    final_results.to_excel(output_path, index=False)

    print("RQ1 full model comparison completed successfully.\n")
    print(final_results)


if __name__ == "__main__":
    rq1_full_comparison()

def plot_f1_comparison():
    # Load comparison table
    input_path = os.path.join(
        "tables", "RQ1_Table2_Model_Performance_Raw_vs_Clean.xlsx"
    )

    df = pd.read_excel(input_path)

    # Separate raw and clean
    raw_df = df[df["Data_Version"] == "Raw"]
    clean_df = df[df["Data_Version"] == "Clean"]

    models = raw_df["Model"].values
    f1_before = raw_df["F1_Score"].values
    f1_after = clean_df["F1_Score"].values

    x = range(len(models))
    width = 0.35

    plt.figure(figsize=(8, 5))

    plt.bar(
        [i - width / 2 for i in x],
        f1_before,
        width,
        label="Before",
        color="#f4b400"
    )

    plt.bar(
        [i + width / 2 for i in x],
        f1_after,
        width,
        label="After",
        color="#4aa3df"
    )

    plt.xticks(x, models)
    plt.ylabel("F1-score")
    plt.title("Figure 4: F1-score Before vs After Cleaning")
    plt.legend()
    plt.tight_layout()

    output_path = os.path.join("figures", "RQ1_Figure_4_model_Comparison.pdf")
    os.makedirs("figures", exist_ok=True)
    plt.savefig(output_path)
    plt.close()

    print("Figure 4 (F1-score comparison) generated successfully.")


if __name__ == "__main__":
    plot_f1_comparison()

'''
Random Forest is the better-performing model overall, particularly after data cleaning, 
as it achieves higher F1-score and accuracy compared to Logistic Regression.

'''
