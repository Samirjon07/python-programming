import pandas as pd

d=pd.read_csv(r"C:\Users\User\OneDrive\Рабочий стол\Excel data files\covid-vaccination-vs-death_ratio (2).csv")

d1=d.iloc[10:16,[0,2]]

d2=d.max()
print(d2)

print(d1)
