import pandas as pd

def add_age_groups(df):
    df = df.copy()
    df["AgeGroup"] = pd.cut(
        df["Age"],
        bins=[0, 45, 60, 120],
        labels=["Young (<45)", "Middle (45–60)", "Older (>60)"]
    )
    return df
