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



rev=""
s=input("input string")
rev = s[::-1]
if rev==s:
   print("palindrome")
else:
   print("not palindrome")

  
