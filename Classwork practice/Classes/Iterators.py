tuple=("1","2","3","4","5")
iterator=iter(tuple)

print(next(iterator))#1
print(next(iterator))#2
print(next(iterator))#3
print(next(iterator))#4
print(next(iterator))#5
#print(next(iterator)) this one will give a mistake


#Looping throught an iterator:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
  
#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):  
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))