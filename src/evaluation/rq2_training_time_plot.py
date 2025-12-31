import os
import joblib
import matplotlib.pyplot as plt
import pandas as pd

def generate_plot():
    figures_dir = "figures"
    os.makedirs(figures_dir, exist_ok=True)

    times = joblib.load("models/training_time.pkl")
    perf = pd.read_excel("tables/RQ2_Table_3_Model_Performance.xlsx")

    plt.figure()
    plt.scatter(times.values(), perf["Accuracy"])
    for model, t in times.items():
        acc = perf.loc[perf["Model"] == model, "Accuracy"].values[0]
        plt.text(t, acc, model)

    plt.xlabel("Training Time (seconds)")
    plt.ylabel("Accuracy")
    plt.title("RQ2: Performance vs Training Time")
    plt.savefig("figures/RQ2_Figure_5_Accuracy_vs_Time.pdf")
    plt.close()

if __name__ == "__main__":
    generate_plot()
