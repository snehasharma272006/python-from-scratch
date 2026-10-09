#loops in python 
#for loop we use rnage fucntion (start, stop,step)
for i in range(0,10,1): #ofc the ending value is excluded and not printed
    print (i)

#or
a=range(0,10,1)
for i in a:
    print(i)


#we have three jump stateents 
#break , continue and pass

#break statement is used to exit the loop when a certain condition is met
#continue statement is used to skip the current iteration and move to the next iteration of the loop
#pass statement is used when we want to write a loop but we don't want to execute any code 


for i in range (0,10):
    if i==5:
        continue
    if i==6:
        pass
    if i==7:
        break
    print (i)


    