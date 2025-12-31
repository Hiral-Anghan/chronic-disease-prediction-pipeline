import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_plot():
    os.makedirs("figures", exist_ok=True)

    df = pd.read_excel("tables/RQ4_Table_9_Performance_By_Age_Group.xlsx")

    plt.figure()
    plt.bar(df["AgeGroup"], df["Accuracy"])
    plt.ylabel("Accuracy")
    plt.title("RQ4 Figure 11: Accuracy by Age Group")
    plt.tight_layout()
    plt.savefig("figures/RQ4_Figure_11_Accuracy_By_Age_Group.pdf")
    plt.close()

    print("RQ4 Figure 11 generated successfully.")

if __name__ == "__main__":
    generate_plot()
