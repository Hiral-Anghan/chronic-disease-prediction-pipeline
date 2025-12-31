import os
import matplotlib.pyplot as plt

def generate_ethical_risk_summary():
    os.makedirs("figures", exist_ok=True)

    risks = [
        "Sex-based bias",
        "Age-based bias",
        "Data imbalance",
        "Model opacity",
        "Unequal error rates"
    ]

    severity = [3, 4, 4, 3, 5]  # relative ethical risk levels (1–5)

    plt.figure(figsize=(8, 5))
    bars = plt.barh(risks, severity)

    plt.xlabel("Ethical Risk Severity (Low → High)")
    plt.title("RQ4 Figure 12: Ethical Risk Summary Diagram")

    for bar, value in zip(bars, severity):
        plt.text(value + 0.1, bar.get_y() + bar.get_height()/2,
                 str(value), va="center")

    plt.xlim(0, 6)
    plt.tight_layout()
    plt.savefig("figures/RQ4_Figure_12_Ethical_Risk_Summary.pdf")
    plt.close()

    print("RQ4 Figure 12 generated successfully.")

if __name__ == "__main__":
    generate_ethical_risk_summary()
