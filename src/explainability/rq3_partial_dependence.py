import os
import joblib
import matplotlib.pyplot as plt
from sklearn.inspection import PartialDependenceDisplay

def generate_pdp():
    os.makedirs("figures", exist_ok=True)

    rf = joblib.load("models/random_forest.pkl")
    X_test, _, _ = joblib.load("models/test_data.pkl")

    # Convert integer columns to float (future-proof)
    X_test = X_test.astype(float)

    features = X_test.columns[:3]

    fig, ax = plt.subplots(figsize=(10, 4))
    PartialDependenceDisplay.from_estimator(
        rf,
        X_test,
        features,
        ax=ax
    )

    plt.suptitle("RQ3 Figure 9: Partial Dependence Plots")
    plt.tight_layout()
    plt.savefig("figures/RQ3_Figure_9_Partial_Dependence.pdf")
    plt.close()

    print("RQ3 Figure 9 generated successfully.")

if __name__ == "__main__":
    generate_pdp()
