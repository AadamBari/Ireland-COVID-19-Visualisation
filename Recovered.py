# Recovered cases and deaths from COVID-19 in Ireland

import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import pandas as pd

#### -----(Download data)----
DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(DATASET)
# print(df.head(3))  

#### -----(Select data for ireland)----
df_ireland = df[df['Country'] == 'Ireland']
# print(df_ireland.head(3))

#### -----(Plot data)----

# Colour background
fig, axes = plt.subplots(facecolor='xkcd:cream')
axes.set_facecolor('xkcd:cream')

# Plot columns 'Recovered', 'Confirmed' and 'Deaths'
df_ireland.plot(x = 'Date', y = 'Confirmed', color = 'blue', ax = axes)
df_ireland.plot(x = 'Date', y = 'Recovered', color = 'green', ax = axes)
df_ireland.plot(x = 'Date', y = 'Deaths', color = 'red', ax = axes)


plt.xticks(rotation=45) # rotate date labels
plt.show()