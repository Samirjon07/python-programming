f=open("a.txt","w")
f.write("Hello World")
f.close()

f=open("a.txt","r")
print(f.read(5))
f.close()

f=open("a.txt","a")
f.write("\nSamirjon Tursunov")
f.close()

f=open("a.txt","r")
print(f.read())
f.close()