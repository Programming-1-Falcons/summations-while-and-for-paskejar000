#for Summation code here
n = int(input("Enter a number: "))
total = 0

if n >= 0: # make sure range is going right way
    step = 1
else:
    step = -1
    
print("Adding",end=' ')
for i in range(1,n+1,step): #for loop from 1 to n
    if i != n: # format print to be on one line
        print(i,end=' + ')
    else:
        print(i)
    total += i
print("Summation Total:",total)
