
def isprime(x):
    for i in range(2,int(pow(x,0.5))+1):
        if x%i == 0:
           return False
    if x==1 or x==0:
        return False
    else:
        return True
    


p=[0]
for i in range(10000):
    if isprime(i):
        p.append(i)
#print(p[:100])        

f=[0,1,1]
for i in range(3,100):
    g=f[i-1]+f[i-2]
    f.append(g)
#print(f)

l=[0]
for i in range(1,100):
    l.append(f[i])
    l.append(p[i])
#print(l)


n=int(input())
print(l[n])

   
