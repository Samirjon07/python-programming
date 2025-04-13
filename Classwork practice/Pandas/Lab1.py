import pandas as pd

d=pd.read_csv(r"C:\Users\User\OneDrive\Рабочий стол\Excel data files\covid-vaccination-vs-death_ratio (2).csv")

d1=d[d["people_fully_vaccinated"]<200000]

print(d1)