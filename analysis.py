# khiati walid _ Yasser test
import pandas as pd
from pandas_profiling import ProfileReport
import geopy.distance
from datetime import datetime

df = pd.read_csv("Use_Case.csv")
# profile = ProfileReport(df, title="Yasser Test Analysis Report", explorative=True)
# profile.to_file(output_file=" usecase.html")

# delete duplciates
df.drop_duplicates(subset=None, keep="first", inplace=True)

# delete rows that has empty variables
df.dropna(inplace=True)

# refactor timestamp columns to default %M:%S:%f
df["when_the_delivery_started"] = df["when_the_delivery_started"].str.replace(
    ".", ":", regex=False
)

df["when_the_courier_arrived_at_pickup"] = df[
    "when_the_courier_arrived_at_pickup"
].str.replace(".", ":", regex=False)

df["when_the_courier_left_pickup"] = df["when_the_courier_left_pickup"].str.replace(
    ".", ":", regex=False
)

df["when_the_courier_arrived_at_dropoff"] = df[
    "when_the_courier_arrived_at_dropoff"
].str.replace(".", ":", regex=False)






# refactor data string columns to datetime structure
df["when_the_delivery_started"] = pd.to_datetime(
    df["when_the_delivery_started"], format="%M:%S:%f"
).dt.time

df["when_the_courier_arrived_at_pickup"] = pd.to_datetime(
    df["when_the_courier_arrived_at_pickup"], format="%M:%S:%f"
).dt.time

df["when_the_courier_left_pickup"] = pd.to_datetime(
    df["when_the_courier_left_pickup"], format="%M:%S:%f"
).dt.time

df["when_the_courier_arrived_at_dropoff"] = pd.to_datetime(
    df["when_the_courier_arrived_at_dropoff"], format="%M:%S:%f"
).dt.time


# drop illogic rows concerning timing columns
df = df[df["when_the_courier_arrived_at_dropoff"] > df["when_the_courier_left_pickup"]]
df = df[df["when_the_courier_arrived_at_pickup"] > df["when_the_delivery_started"]]


# finding the distance between picking up and dropping place*
df["distance_crossed"] = df["pickup_lon"]
for i in range(len(df.index)):
    df["distance_crossed"].iloc[i] = geopy.distance.geodesic(
        (df["pickup_lat"].iloc[i], df["pickup_lon"].iloc[i]),
        (df["dropoff_lat"].iloc[i], df["dropoff_lon"].iloc[i]),
    ).km


# finding how long the courrier took in his journey


profile2 = ProfileReport(df, title="Yasser Test Analysis Report", explorative=True)
profile2.to_file(output_file=" usecase_2.html")


df.to_csv("usecase_cleaned.csv")
