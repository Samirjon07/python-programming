x = 300#global
def myfunc():
  print(x)

myfunc()
print(x)



x = 300#gloabal
def myfunc():
  x = 200#local
  print(x)

myfunc()
print(x)


x = 300
def myfunc():
  global x #making it global
  x = 200

myfunc()
print(x)


#The nonlocal keyword is used to work with variables inside nested functions.
#The nonlocal keyword makes the variable belong to the outer function.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())