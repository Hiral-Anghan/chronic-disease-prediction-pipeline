import pandas as pd
import os

def generate_table():
    tables_dir = "tables"
    os.makedirs(tables_dir, exist_ok=True)

    df = pd.DataFrame([
        {
            "Model": "Logistic Regression",
            "Interpretability": "High",
            "Explanation_Method": "Model coefficients"
        },
        {
            "Model": "Random Forest",
            "Interpretability": "Medium",
            "Explanation_Method": "Feature importance"
        }
    ])

    df.to_excel("tables/RQ2_Table_6_Interpretability_Comparison.xlsx", index=False)

if __name__ == "__main__":
    generate_table()
