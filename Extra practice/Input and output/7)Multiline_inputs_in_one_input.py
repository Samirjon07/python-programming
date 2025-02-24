'''
Write a program to take three names as input from a user in the single input() function call.

Expected Output

Enter three string Emma Jessa Kelly
Name1: Emma
Name2: Jessa
Name3: Kelly
'''

names=str(input("Enter three names with space between them:  "))
names=names.split(" ")
print("\nName1:",names)# Name1: ['sasa', 'sasas', 'sasas'] it will create a list of names
#to access to names use indexing
print("\nName1:",names[0])
print("\nName2:",names[1])
print("\nName3:",names[2])


'''Answer:

str1, str2, str3 = input("Enter three string").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)
'''