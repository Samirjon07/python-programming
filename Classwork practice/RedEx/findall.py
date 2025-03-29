import re

txt= "Samirjon Tursunov is a student of SIUT and SIUT is a university"

x=re.findall("SIUT",txt)
y=re.search("SIUT",txt)
z=re.split("SIUT",txt)
t=re.sub("SIUT","UNIVERSITY",txt)

print("\n",x)
print("\n",y)
print("\n",z)
print("\n",t)