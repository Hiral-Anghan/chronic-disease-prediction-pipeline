import os
import joblib
import pandas as pd
from sklearn.metrics import confusion_matrix

def generate_tables():
    models_dir = "models"
    tables_dir = "tables"
    os.makedirs(tables_dir, exist_ok=True)

    lr = joblib.load(f"{models_dir}/logistic_regression.pkl")
    rf = joblib.load(f"{models_dir}/random_forest.pkl")
    scaler = joblib.load(f"{models_dir}/scaler.pkl")
    X_test, X_test_scaled, y_test = joblib.load(f"{models_dir}/test_data.pkl")

    lr_cm = confusion_matrix(y_test, lr.predict(X_test_scaled))
    rf_cm = confusion_matrix(y_test, rf.predict(X_test))

    pd.DataFrame(lr_cm).to_excel("tables/RQ2_Table_4_LR_Confusion_Matrix.xlsx")
    pd.DataFrame(rf_cm).to_excel("tables/RQ2_Table_5_RF_Confusion_Matrix.xlsx")

if __name__ == "__main__":
    generate_tables()
