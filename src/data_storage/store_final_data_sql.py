import pandas as pd
import joblib
from sqlalchemy import create_engine

TARGET = "HeartDisease"

def store_final_data():
    # Load clean data
    df = pd.read_csv("data/processed/clean_data.csv")

    # Load final model
    rf = joblib.load("models/random_forest.pkl")

    X = pd.get_dummies(df.drop(columns=[TARGET]), drop_first=True)
    df["Prediction"] = rf.predict(X)

    # MySQL connection (UPDATE credentials if needed)
    engine = create_engine(
    "mysql+pymysql://pipeline_user:pipeline_pass@localhost:3306/chronic_disease_db"
)

    # Store final analytical dataset
    df.to_sql(
        name="final_heart_disease_analytics",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Final analytical dataset stored in MySQL.")

if __name__ == "__main__":
    store_final_data()
