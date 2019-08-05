"""
n=int(input())

for i in range(n):
    c=1
    for j in range(i+1):
        print(c,end="")
        c+=1
    print()    
"""

n=int(input())

for i in range(n):
    c="a"
    for j in range(i+1):
        print(c,end="")
        c=chr(ord(c)+1)
    print()    
