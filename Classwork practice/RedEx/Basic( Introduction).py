import re

txt="Samirjon Tursunov is a student of SIUT"

x=re.search("SIUT",txt)

if x:
    print("SIUT is present in the string")
    
else:
    print("SIUT is not present in the string")