import os
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve

def generate_roc():
    figures_dir = "figures"
    os.makedirs(figures_dir, exist_ok=True)

    lr = joblib.load("models/logistic_regression.pkl")
    rf = joblib.load("models/random_forest.pkl")
    scaler = joblib.load("models/scaler.pkl")
    X_test, X_test_scaled, y_test = joblib.load("models/test_data.pkl")

    lr_fpr, lr_tpr, _ = roc_curve(y_test, lr.predict_proba(X_test_scaled)[:, 1])
    rf_fpr, rf_tpr, _ = roc_curve(y_test, rf.predict_proba(X_test)[:, 1])

    plt.figure()
    plt.plot(lr_fpr, lr_tpr, label="Logistic Regression")
    plt.plot(rf_fpr, rf_tpr, label="Random Forest")
    plt.legend()
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("RQ2: ROC Curve Comparison")
    plt.savefig("figures/RQ2_Figure_4_ROC_Comparison.pdf")
    plt.close()

if __name__ == "__main__":
    generate_roc()
