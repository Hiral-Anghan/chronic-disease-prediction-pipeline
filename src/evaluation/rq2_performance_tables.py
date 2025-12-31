import os
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score

def generate_table():
    models_dir = "models"
    tables_dir = "tables"
    os.makedirs(tables_dir, exist_ok=True)

    lr = joblib.load(f"{models_dir}/logistic_regression.pkl")
    rf = joblib.load(f"{models_dir}/random_forest.pkl")
    scaler = joblib.load(f"{models_dir}/scaler.pkl")
    X_test, X_test_scaled, y_test = joblib.load(f"{models_dir}/test_data.pkl")

    data = [
        {
            "Model": "Logistic Regression",
            "Accuracy": accuracy_score(y_test, lr.predict(X_test_scaled)),
            "F1_Score": f1_score(y_test, lr.predict(X_test_scaled))
        },
        {
            "Model": "Random Forest",
            "Accuracy": accuracy_score(y_test, rf.predict(X_test)),
            "F1_Score": f1_score(y_test, rf.predict(X_test))
        }
    ]

    df = pd.DataFrame(data)
    df.to_excel("tables/RQ2_Table_3_Model_Performance.xlsx", index=False)

if __name__ == "__main__":
    generate_table()
