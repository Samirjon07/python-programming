f=open("a.txt","r")
print(f.readline())

for x in f:
    print(x)
    
f.close()