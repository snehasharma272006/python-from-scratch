
# PYTHON WHILE LOOP PRACTICE


# Q1. Print numbers from 1 to 10 using a while loop.

i = 1
while i <= 10:
print(i)
i += 1

# Q2. Print numbers from 10 to 1 in reverse order.

i = 10
while i >= 1:
print(i)
i -= 1

# Q3. Print the multiplication table of a number entered by the user.

num = int(input("Enter a number: "))
i = 1

while i <= 10:
print(num, "x", i, "=", num * i)
i += 1


# Q4. Find the sum of numbers from 1 to n.

# Example: n = 5, Output = 15

n = int(input("Enter a positive number: "))
i = 1
total = 0

while i <= n:
total += i
i += 1

print("Sum:", total)

# Q5. Count the number of digits in an integer.

# Example: Input = 5832, Output = 4

num = int(input("Enter an integer: "))
num = abs(num)
count = 0

while num > 0:
count += 1
num //= 10

# Special case: zero has one digit.

if count == 0:
count = 1

print("Number of digits:", count)

# Q6. Reverse a number using a while loop.

# Example: Input = 1234, Output = 4321

num = int(input("Enter an integer: "))
sign = -1 if num < 0 else 1
num = abs(num)
reverse = 0

while num > 0:
digit = num % 10
reverse = reverse * 10 + digit
num //= 10

print("Reversed number:", sign * reverse)

