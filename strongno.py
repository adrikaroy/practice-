n=int(input())
m=n
def fact(p):
    x=1
    for i in range(2,p+1):
        x=x*i
    return(x)    
s=0
while(n>0):
    p=n%10
    s+=fact(p)
    n=n//10

if (s==m):
    print("Strong")
else:
    print("not")
      
