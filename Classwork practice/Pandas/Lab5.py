import pandas as pd
d=pd.Series({'k':10,'k2':20})
print(d)


d2=pd.Series([10,20,30],index=['a','b','c'])
print(d2)


d3=pd.DataFrame({"Name":["Mohammad","Gouse","Galety"],"Course":["Cs1","Cs2","cs3"]})
print(d3)