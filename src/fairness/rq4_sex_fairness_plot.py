import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_plot():
    os.makedirs("figures", exist_ok=True)

    df = pd.read_excel("tables/RQ4_Table_8_Performance_By_Sex.xlsx")

    plt.figure()
    plt.bar(df["Sex"], df["Accuracy"])
    plt.ylabel("Accuracy")
    plt.title("RQ4 Figure 10: Accuracy by Sex")
    plt.tight_layout()
    plt.savefig("figures/RQ4_Figure_10_Accuracy_By_Sex.pdf")
    plt.close()

    print("RQ4 Figure 10 generated successfully.")

if __name__ == "__main__":
    generate_plot()
