# call necessary packages:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# call data:
gdpdata = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

# Variable to plot:
# ‘Mortality rate, infant (per 1,000 live births)’
# ‘GDP per capita (constant 2010 US$)’
# ‘Country Name’

gdpdata.plot.scatter(
    y="Mortality rate, infant (per 1,000 live births)",
    x="GDP per capita (constant 2010 US$)",
)

# Display the plot
plt.show()
