import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

df_middlesex_county_covid = pd.read_csv(r'covid19_middlesex_county.csv')
#df_middlesex_county_covid['Everyday case average'] = df_middlesex_county_covid['Everyday new cases'].rolling(window=3).mean()

print(df_middlesex_county_covid)

#middlesex_pop = 1604994


style.use('ggplot')
#df_middlesex_county_covid['Everyday new cases'].plot(kind='bar')
#plt.minorticks_off()
plt.bar(df_middlesex_county_covid['date'], df_middlesex_county_covid['Everyday new cases'], align='center',
color='black', edgecolor='green')
plt.plot(df_middlesex_county_covid['date'], df_middlesex_county_covid['Everyday case average'], color='red')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='yellow')
plt.title("Everyday new cases in Middlesex County")
plt.xticks(rotation=90)
plt.xlabel("Date")
plt.ylabel("No. of new cases")
plt.legend(loc='upper center')

plt.show()

df_middlesex_county_covid['Everyday new deaths'].plot(kind='bar')
plt.plot(df_middlesex_county_covid['date'], df_middlesex_county_covid['Everyday death average'], color='black')
plt.minorticks_off()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
plt.title("Everyday new deaths in Middlesex County")
plt.xlabel("Days")
plt.ylabel("Deaths")

plt.show()