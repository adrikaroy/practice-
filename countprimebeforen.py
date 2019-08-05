n=int(input())
s=0
for i in range(2,n):
    c=0
    for j in range(2,(int(pow(i,0.5))+1)):
        if(i%j==0):
            c=c+1
    if c==0:
        s=s+1
print(s)                   






