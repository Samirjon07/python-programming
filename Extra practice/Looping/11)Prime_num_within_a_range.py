'''
Print all prime numbers within a range
Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

Examples:

6 is not a prime number because it can be made by 2×3 = 6
37 is a prime number because no other whole numbers multiply to make it.
Given:

# range
start = 25
end = 50
Expected output:

Prime numbers between 25 and 50 are:
29
31
37
41
43
47
'''
start=int(input())
end=int(input())
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)