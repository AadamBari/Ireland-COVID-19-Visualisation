import matplotlib.pyplot as plt
import pandas as pd

# Download Data
DATASET = r'http://opendata-geohive.hub.arcgis.com/datasets/d9be85b30d7748b5b7c09450b8aede63_0.csv?outSR={%22latestWkid%22:3857,%22wkid%22:102100}'
df = pd.read_csv(DATASET)
# print(df.info())
# print(df.head(3))  

# select relevant columns
df1 = df[["CountyName", "PopulationCensus16", "ConfirmedCovidCases"]].copy()

# Create a properly formatted date column
# split the timestamp to seperate time and date
# the expand parameter is set to True, which means it will return a data frame with all separated strings in different columns.
# extract the date into a new columns
datetime = df["TimeStamp"].str.split(" ", n=1, expand=True)
df1["Date"] = datetime[0]

# get list of unique county names 
counties = pd.unique(df1["CountyName"])

cases_per_county = []

# get the latest number of cases per county
for county in counties:
   county_df = df1[df1.CountyName == county]
   cases_per_county.append(county_df['ConfirmedCovidCases'].iloc[-1])

# Create the x position for county labels
x_pos = [i for i, _ in enumerate(counties)]
# x_pos = list(range(len(counties))) # alternative

# Create the bar chart
plt.style.use('ggplot')
plt.barh(x_pos, cases_per_county, color='red')
plt.ylabel("County")
plt.xlabel("Number of Cases")
plt.title("Covid-19 Cases per County in the Republic of Ireland")

plt.yticks(x_pos, counties)

plt.show()
