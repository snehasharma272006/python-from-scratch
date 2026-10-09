# to check wheather a number is a perfet number or not 

factor=0
n=int(input("enter n "))
for i in range (1, n):
    if n%i==0:
        factor=factor+i
print("sum of factors of", n, "are", factor)    
if factor==n:
     print("no is perfect number")
else:
    print("no is not perfect number")




n = int(input("enter number: "))

is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("prime")
else:
    print("not prime")


#plaindrome checking
rev=""
s=input("input string")
rev = s[::-1]
if rev==s:
   print("palindrome")
else:
   print("not palindrome")



count =0
s=input("enetr string")
for i in range(len(s)): #len function gives the length of the string
    count = count +1


print("no of charcater sin a string are " , count)



#classify letters, numbers , special chzrcaters 

s = "P@#yn26at^&i5ve"

letters = 0
digits = 0
symbols = 0

for ch in s:
    a = ord(ch)

    if (65 <= a <= 90) or (97 <= a <= 122):
        letters += 1
    elif 48 <= a <= 57:
        digits += 1
    else:
        symbols += 1

print("Letters:", letters)
print("Digits:", digits)
print("Symbols:", symbols)


s = "P@#yn26at^&i5ve"

letters = digits = symbols = 0

for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        symbols += 1

print("Letters:", letters)
print("Digits:", digits)
print("Symbols:", symbols)
  
#seperate each dignit of a number and print it on new line 

