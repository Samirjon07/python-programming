from numpy import random 

x=random.choice([3,5,7,9],size=(100))
print("\n",x)#it will generate 100 number which are


x=random.choice([3,5,7,9],size=(100),p=[0.1,0.3,0.4,0.2])
print("\n",x)#p shows probability: 0.1 means 10 %


x=random.choice([3,5,7,9],size=(2,3),p=[0.1,0.3,0.4,0.2])
print("\n",x)# we have creats 2*3 matrix


