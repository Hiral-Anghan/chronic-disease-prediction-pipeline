import os
import joblib
import shap
import matplotlib.pyplot as plt
import numpy as np

def generate_shap_summary():
    os.makedirs("figures", exist_ok=True)

    rf = joblib.load("models/random_forest.pkl")
    X_test, _, _ = joblib.load("models/test_data.pkl")

    explainer = shap.TreeExplainer(rf)
    shap_values = explainer.shap_values(X_test)

    # ---- HANDLE SHAP OUTPUT SHAPE SAFELY ----
    if isinstance(shap_values, list):
        # Binary classification: take positive class
        shap_matrix = shap_values[1]
    elif len(shap_values.shape) == 3:
        # Newer SHAP versions: (samples, features, classes)
        shap_matrix = shap_values[:, :, 1]
    else:
        shap_matrix = shap_values

    shap.summary_plot(
        shap_matrix,
        X_test,
        show=False
    )

    plt.title("RQ3 Figure 7: SHAP Summary Plot")
    plt.tight_layout()
    plt.savefig("figures/RQ3_Figure_7_SHAP_Summary.pdf")
    plt.close()

    print("RQ3 Figure 7 generated successfully.")

if __name__ == "__main__":
    generate_shap_summary()
