
"""
s=int(input())
n=int(input())
l=list(map(int, input().split()))
c=0

for i in range(len(l)-1):
    if i!=(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==s:
                c=c+1

print(c)
"""

s=int(input())
n=int(input())
l=list(map(int, input().split()))
p=0

a=sorted(l)
b=a[0]
c=a[len(a)-1]
print(b,c)

while(b<c):
    
    if b+c==s:
        p=p+1
        b+=1              
        
    elif (b+c) > s:
        c=c-1
    elif (b+c) < s:
        b=b+1
            
            
print(p)        
        
