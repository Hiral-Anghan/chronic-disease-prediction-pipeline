import os
import joblib
import shap
import matplotlib.pyplot as plt
import numpy as np

def generate_local_shap():
    os.makedirs("figures", exist_ok=True)

    rf = joblib.load("models/random_forest.pkl")
    X_test, _, _ = joblib.load("models/test_data.pkl")

    explainer = shap.TreeExplainer(rf)
    shap_values = explainer.shap_values(X_test)

    if isinstance(shap_values, list):
        shap_matrix = shap_values[1]
        expected_value = explainer.expected_value[1]
    elif len(shap_values.shape) == 3:
        shap_matrix = shap_values[:, :, 1]
        expected_value = explainer.expected_value[1]
    else:
        shap_matrix = shap_values
        expected_value = explainer.expected_value

    shap.force_plot(
        expected_value,
        shap_matrix[0],
        X_test.iloc[0],
        matplotlib=True,
        show=False
    )

    plt.title("RQ3 Figure 8: Local SHAP Explanation")
    plt.savefig("figures/RQ3_Figure_8_Local_SHAP.pdf")
    plt.close()

    print("RQ3 Figure 8 generated successfully.")

if __name__ == "__main__":
    generate_local_shap()
