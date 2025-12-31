import os
import pandas as pd

def generate_table():
    tables_dir = "tables"
    os.makedirs(tables_dir, exist_ok=True)

    data = [
        {
            "Feature": "Age",
            "Clinical_Relevance": "Older age increases cardiovascular risk"
        },
        {
            "Feature": "Cholesterol",
            "Clinical_Relevance": "High cholesterol is linked to atherosclerosis"
        },
        {
            "Feature": "RestingBP",
            "Clinical_Relevance": "Hypertension increases heart disease risk"
        },
        {
            "Feature": "MaxHR",
            "Clinical_Relevance": "Lower max heart rate indicates reduced cardiac fitness"
        },
        {
            "Feature": "Oldpeak",
            "Clinical_Relevance": "ST depression reflects myocardial ischemia"
        }
    ]

    df = pd.DataFrame(data)
    df.to_excel("tables/RQ3_Table_7_Key_Features_Clinical_Justification.xlsx", index=False)

    print("RQ3 Table 7 generated.")

if __name__ == "__main__":
    generate_table()
