import os
import time
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

TARGET = "HeartDisease"

def train_models():
    data_path = os.path.join("data", "processed", "clean_data.csv")
    models_dir = "models"
    os.makedirs(models_dir, exist_ok=True)

    df = pd.read_csv(data_path)

    X = pd.get_dummies(df.drop(columns=[TARGET]), drop_first=True)
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Logistic Regression
    start = time.time()
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train_scaled, y_train)
    lr_time = time.time() - start

    # Random Forest
    start = time.time()
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    rf_time = time.time() - start

    joblib.dump(lr, f"{models_dir}/logistic_regression.pkl")
    joblib.dump(rf, f"{models_dir}/random_forest.pkl")
    joblib.dump(scaler, f"{models_dir}/scaler.pkl")
    joblib.dump((X_test, X_test_scaled, y_test), f"{models_dir}/test_data.pkl")
    joblib.dump(
        {"Logistic Regression": lr_time, "Random Forest": rf_time},
        f"{models_dir}/training_time.pkl"
    )

    print("RQ2: Models trained successfully.")

if __name__ == "__main__":
    train_models()
