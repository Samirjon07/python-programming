import pandas as pd
d=pd.read_csv(r"C:\Users\User\OneDrive\Рабочий стол\Excel data files\covid-vaccination-vs-death_ratio (2).csv")

d1=d.loc[10:15,("country","people_fully_vaccinated")]
print(d1)