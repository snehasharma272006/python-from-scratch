#accepting an integer and printing hello n times
n=int(input("enter n :"))
for i in range(n):
    print("hello")


#printing natural numbers upto n 
n = int(input("enter n ")) 
for i in range(1,n+1):
    print(i)

#reverse loop
for i in range(10, 1, -1):
    print(i)

#table of a number
n=int(input("enter n "))
for i in range (1,n+1):
    print(n , "*", i , "=", n*i)


#sum of first n natural numbers
n=int(input("enter n "))
sum = 0
for i in range (1, n+1):
    sum = sum + i
print("sum of first", n, "natural numbers is", sum)


# factorial of a number
n=int(input("enter n "))
fact =1
for i in range (1, n+1):
    fact=fact*i
print("factorial of", n, "is", fact)


n = int(input("enter no: "))
oddsum =0
evensum =0
for i in range (0, n+1):
   if i%2==0:
      evensum= evensum+i
   else: 
    oddsum=oddsum+i

print("even and odd sum are " , evensum , oddsum)


#factors of a number
n = int(input("enter no:"))
for i in range (1, n+1):
   if n%i==0:
       print(i)


       
