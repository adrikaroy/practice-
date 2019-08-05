n,q=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=[]
m=[0]
for i in range(len(a)):
    s.append(a[i]*b[i])

c=0    
for i in s:
    c+=i
    m.append(c)


for i in range(q):
    l,r=map(int,input().split())
    
    print(m[r]-m[l-1])
