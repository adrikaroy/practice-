"""
n= int(input())
a= [str(x) for x in input().split()]
s= input()
r="".join(a)                    
for i in range(len(a)):
    if s not in a:
        print("NO OCCURANCES")
    else:
        l=a.index(s)
        
        u=r.rfind(s)
print(l,"",u)
    
"""

n= int(input())
a= [int(x) for x in input().split()]
s= int(input())

if s not in a:
    print("NO OCCURANCES")
else:
    for i in range(len(a)):
        if a[i] == s:           
            l=i
            break

    for i in range(len(a)-1,-1,-1):
        if a[i] == s:
            u=i
            break
        
    print(l,"",u)
