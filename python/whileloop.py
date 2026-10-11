# Python while loop practice

# Print numbers from 1 to 10.

i = 1
while i <= 10:
    print(i)
    i += 1


# Print all even numbers from 1 to 20.

i = 2
while i <= 20:
    print(i)
    i += 2


# Print the multiplication table of a number entered by the user.

num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1


# Find the sum of numbers from 1 to n.

n = int(input("Enter a positive number: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum:", total)


# Count the number of digits in a positive integer.

num = int(input("Enter a positive integer: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)


# Reverse a positive integer.

num = int(input("Enter a positive integer: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed number:", reversed_num)
