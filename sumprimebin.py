"""
l,r=map(int, input().split())
s=0
for i in range(l,r+1):
    b=bin(i)
    
    c=0
    d=0
    p=list(str(b))
    
    for k in range(2,len(p)):
        if p[k]=='1':
            d+=1
    
    if d>1:    
        for j in range(2,(int(pow(d,0.5))+1)):
            if(d%j==0):
                c=c+1             
        if c==0:
            s=s+1
print(s)                   
"""


    
