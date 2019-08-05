

"""

# a[i]= a[i-1]+a[i-2]
# fib(i)=fib(i-1)+fib(i-2)

def fib(n):
    if n==0:
        return(0)
    elif n==1:
        return(1)
    else:
        return(fib(n-1)+fib(n-2))

n=int(input())
for i in range(n):
    print(fib(i))
        
        
"""

#!/bin/python3

import math

def diagonalDifference(arr):
    # Write your code here
    s,c=0,0
    t=0
    for i in range(n):
        for j in range(n):
            if (i==j):
                print(arr[i][j])
                s+=arr[i][j]
            elif (i+j==n-1):
                print(arr[i][j])
                c+=arr[i][j]
            
    t=abs(s-c)
    return(s,c,t)

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)


