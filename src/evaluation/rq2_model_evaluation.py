import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score, f1_score, roc_curve, auc

TARGET = "HeartDisease"

def evaluate_models():
    data_path = os.path.join("data", "processed", "clean_data.csv")
    models_dir = "models"
    figures_dir = "figures"
    tables_dir = "tables"

    os.makedirs(figures_dir, exist_ok=True)
    os.makedirs(tables_dir, exist_ok=True)

    df = pd.read_csv(data_path)
    X = pd.get_dummies(df.drop(columns=[TARGET]), drop_first=True)
    y = df[TARGET]

    lr = joblib.load(os.path.join(models_dir, "logistic_regression.pkl"))
    rf = joblib.load(os.path.join(models_dir, "random_forest.pkl"))
    scaler = joblib.load(os.path.join(models_dir, "scaler.pkl"))

    X_scaled = scaler.transform(X)

    lr_preds = lr.predict(X_scaled)
    rf_preds = rf.predict(X)

    results = pd.DataFrame([
        {
            "Model": "Logistic Regression",
            "Accuracy": accuracy_score(y, lr_preds),
            "F1_Score": f1_score(y, lr_preds),
            "Interpretability": "High (coefficients)"
        },
        {
            "Model": "Random Forest",
            "Accuracy": accuracy_score(y, rf_preds),
            "F1_Score": f1_score(y, rf_preds),
            "Interpretability": "Medium (feature importance)"
        }
    ])

    results.to_excel(
        os.path.join(tables_dir, "RQ2_Table_3_Model_Comparison.xlsx"),
        index=False
    )

    # ROC Curves
    lr_fpr, lr_tpr, _ = roc_curve(y, lr.predict_proba(X_scaled)[:, 1])
    rf_fpr, rf_tpr, _ = roc_curve(y, rf.predict_proba(X)[:, 1])

    plt.figure()
    plt.plot(lr_fpr, lr_tpr, label="Logistic Regression")
    plt.plot(rf_fpr, rf_tpr, label="Random Forest")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("RQ2: ROC Curve Comparison")
    plt.legend()
    plt.savefig(os.path.join(figures_dir, "RQ2_Figure_4_ROC_Comparison.pdf"))
    plt.close()

    print("RQ2: Model evaluation completed.")

if __name__ == "__main__":
    evaluate_models()
