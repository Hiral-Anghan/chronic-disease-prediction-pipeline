import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

def generate_feature_importance():
    models_dir = "models"
    figures_dir = "figures"
    os.makedirs(figures_dir, exist_ok=True)

    rf = joblib.load(os.path.join(models_dir, "random_forest.pkl"))
    X_test, _, _ = joblib.load(os.path.join(models_dir, "test_data.pkl"))

    importances = rf.feature_importances_
    features = X_test.columns

    fi_df = pd.DataFrame({
        "Feature": features,
        "Importance": importances
    }).sort_values(by="Importance", ascending=False).head(10)

    plt.figure(figsize=(8, 5))
    plt.barh(fi_df["Feature"], fi_df["Importance"])
    plt.xlabel("Importance Score")
    plt.title("RQ3 Figure 6: Global Feature Importance (Random Forest)")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("figures/RQ3_Figure_6_Feature_Importance.pdf")
    plt.close()

    print("RQ3 Figure 6 generated.")

if __name__ == "__main__":
    generate_feature_importance()
