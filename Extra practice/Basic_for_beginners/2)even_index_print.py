'''
Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
'''

'''
Original String is  PYnative
Printing only even index chars
P
n
t
v
'''

word=str(input())
print("Original String is",word)
x=1
print("Printing only even index chars")
for x in range(0,len(word),2):
    print(word[x])
   

'''ANSWER:

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])
''' 