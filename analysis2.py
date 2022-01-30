# khiati walid _ Yasser test
import pandas as pd
from pandas_profiling import ProfileReport
from datetime import datetime, timedelta

df = pd.read_csv("usecase_2.csv")


# transform distance to m
df["distance_m"] = df["distance_crossed"] * 100

# transform time to seconds
df["courrier_timing"] = df["courrier_timing"].str.replace(".", ":", regex=False)
df["courrier_timing"] = pd.to_timedelta(df["courrier_timing"])

df["timing_s"] = df["courrier_timing"]
for i in range(len(df.index)):
    df["timing_s"].iloc[i] = timedelta.total_seconds(df["courrier_timing"].iloc[i])


# get courrier performance _speed_
df["courrier_performance"] = (df["distance_m"] / df["timing_s"]) * 1000


profile = ProfileReport(df, title="Yasser Test Analysis Report", explorative=True)
profile.to_file(output_file=" usecase_3.html")



df.to_csv("usecase_final.csv")