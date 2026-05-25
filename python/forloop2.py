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




n=int(input("enter number:"))
for i in range (2, n):
     if n%i==0:
        print("not prime")
    
    
else:
    print("prime")
  
