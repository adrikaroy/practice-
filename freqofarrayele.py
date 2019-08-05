
a=[int(x) for x in input().split()]
c=0
b=sorted(a)
for i in range(len(b)):
    if b[i-1] == b[i]:
        c=c+1    
    else:
        print(c+1)        
        c=0
print(c)
        
"""
a=[int(x) for x in input().split()]
b=[0]*(max(a)+1)
for i in a:
    b[i]+=1
for i in range(len(b)):
    if b[i]!=0:
        print(i,"-----",b[i])



a=[int(x) for x in input().split()]
b={}
for i in a:
    if i in b:
        b[i] +=1
    else:
        b[i]=1
for i in b:
    print(i,"---",b[i])        
"""
