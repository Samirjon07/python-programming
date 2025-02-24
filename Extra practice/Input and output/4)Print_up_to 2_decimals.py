'''
Display float number with 2 decimal places using print()
Given:

num = 458.541315
Expected Output:

458.54
'''

number=float(input("Enter a float number: "))

print("%.2f" % number)#%.2f will print float number with 2 decimal places

print(f'{number:.2f}')#{number:.2f} will print float number with 2 decimal places

print('{:.2f}'.format(number))#{:.2f} will print float number with 2 decimal places
