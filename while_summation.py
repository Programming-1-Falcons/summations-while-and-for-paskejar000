#while summation code following directions from Readme
n = int(input("Enter a number: "))
total = 0

if n >= 0: # make sure step in range is going right way
    step = 1
else:
    step = -1
    
print("Adding",end=' ')
i = 0
while i != n: # loop n times
    i += step
    if i != n: # format print to be on one line
        print(i,end=' + ')
    else:
        print(i)
    total += i
print("Summation Total:",total)
