import matplotlib.pyplot as plt
import pandas as pd

# Download Data
DATASET = r'http://opendata-geohive.hub.arcgis.com/datasets/d9be85b30d7748b5b7c09450b8aede63_0.csv?outSR={%22latestWkid%22:3857,%22wkid%22:102100}'
df = pd.read_csv(DATASET)
# print(df.info())
# print(df.head(3))  

# select relevant columns
df1 = df[["CountyName", "PopulationCensus16", "ConfirmedCovidCases", "PopulationProportionCovidCases", "ConfirmedCovidDeaths", "ConfirmedCovidRecovered"]].copy()

# split the timestamp to seperate time and date
# the expand parameter is set to True, which means it will return a data frame with all separated strings in different columns.
datetime = df["TimeStamp"].str.split(" ", n=1, expand=True)

# extract the date into a new column
df1["Date"] = datetime[0]

# print(df1["Date"])
print(df1.head())

# get unique county names
x = pd.unique(df1["CountyName"])

# Create the x position of the bars
x_pos = [i for i, _ in enumerate(x)]
# x_pos = list(range(len(x)))
print(x_pos)

