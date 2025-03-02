
'''list1 = [10, 20, 30, 40, 50]
Expected output:

50
40
30
20
10
and also reverse list
'''

num=[10,20,30,40,50]
rev=[]
for i in range (len(num)-1,-1,-1):
    print(num[i])
    rev.append(num[i])
print(rev)


"""
list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list
for item in new_list:
    print(item)

"""