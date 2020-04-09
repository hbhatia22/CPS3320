import pandas as pd

# import csv dataset from kaggle using pandas
df = pd.read_csv(r'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
# display the dataframe
print(df.tail(10))

# filter the dataset to show cases in my home county Middlesex
df_middlesex_county = df[df.fips==34023][['date','cases','deaths']].reset_index(drop=True).copy()

# calculate everyday new cases in Middlesex county
df_middlesex_county['Everyday new cases'] = df_middlesex_county.cases.diff()
# calculate everyday new deaths in Middlesex county
df_middlesex_county['Everyday new deaths'] = df_middlesex_county.deaths.diff()

# print the new dataframe
print(df_middlesex_county)

# restructure the dataframe to show columns in desired order
df_middlesex_county_new = df_middlesex_county[['date', 'cases', 'Everyday new cases', 'deaths', 'Everyday new deaths']]
print(df_middlesex_county_new)

# adding case average and death average columns to the data frame
df_middlesex_county_new['Everyday case average'] = df_middlesex_county_new['Everyday new cases'].rolling(window=3).mean()
df_middlesex_county_new['Everyday death average'] = df_middlesex_county_new['Everyday new deaths'].rolling(window=3).mean()

# restructure the dataframe to show columns in desired order
df_middlesex_county_new = df_middlesex_county_new[['date', 'cases', 'Everyday new cases', 'Everyday case average', 'deaths', 'Everyday new deaths','Everyday death average']]
print(df_middlesex_county_new)

# export the dataframe into a csv file
df_middlesex_county_new.to_csv(r'covid19_middlesex_county.csv', index=True, header=True)




