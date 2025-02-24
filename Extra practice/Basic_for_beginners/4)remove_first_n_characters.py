'''
Write a Python code to remove characters from a string from 0 to n and return a new string.

For Example:

remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.
Note: n must be less than the length of the string.
'''

word=str(input("Enter The word: "))
n=int(input("Enter the number of characters you want to delete: "))
def remove_chars(word,n):
    print("Removed version: ",word[n:])
remove_chars(word,n)


'''ANSWER:

def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
'''