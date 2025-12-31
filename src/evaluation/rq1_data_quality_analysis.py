import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

def rq1_data_quality_analysis():
    # Paths
    input_path = os.path.join("data", "processed", "raw_data.csv")
    figures_dir = "figures"
    tables_dir = "tables"

    os.makedirs(figures_dir, exist_ok=True)
    os.makedirs(tables_dir, exist_ok=True)

    # Load raw data
    df = pd.read_csv(input_path)

    if df.empty:
        raise ValueError("Raw dataset is empty.")

    # -----------------------------
    # TABLE 1: Data Quality Report
    # -----------------------------
    data_quality = pd.DataFrame({
        "Missing_Values": df.isnull().sum(),
        "Missing_Percentage": df.isnull().mean() * 100,
        "Unique_Values": df.nunique()
    })

    duplicate_count = df.duplicated().sum()
    data_quality["Summary showing missing values, duplicates, and inconsistencies per feature."] = duplicate_count

    table_path = os.path.join(tables_dir, "RQ1_Table 1.xlsx")
    data_quality.to_excel(table_path)

    # -----------------------------
    # FIGURE 1: Missing Value Heatmap
    # -----------------------------
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False)
    plt.title("A heatmap showing missing values across columns.")
    plt.xlabel("Features")
    plt.ylabel("Records")

    fig1_path = os.path.join(figures_dir, "RQ1_Figure 1.pdf")
    plt.tight_layout()
    plt.savefig(fig1_path)
    plt.close()

    # -----------------------------
    # FIGURE 2: Outlier Boxplots
    # -----------------------------
    numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns

    plt.figure(figsize=(12, 6))
    df[numerical_cols].boxplot(rot=90)
    plt.title("Boxplots illustrating extreme values in features such as cholesterol and blood pressure.")
    plt.ylabel("Value")

    fig2_path = os.path.join(figures_dir, "RQ1_Figure 2.pdf")
    plt.tight_layout()
    plt.savefig(fig2_path)
    plt.close()

    print("RQ1 data quality analysis completed successfully.")


if __name__ == "__main__":
    rq1_data_quality_analysis()
