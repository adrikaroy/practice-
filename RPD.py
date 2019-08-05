t = int(input())
def sod(s):
 c=0
 while(s>0):
  m=s%10
  c+=m
  s=(s//10)
 return(c)

for i in range(t):
 n=int(input())
 a=list(map(int,input().split()))
 if n==1:
  s=a[0]
  print(sod(s))
 elif n==2:
  x=1
  for j in range(n):
   x*=a[j]
  s=x    
  print(sod(s))
 else:     
  l=[]
  for i in range(n-1): 
   x=1   
   for j in range(i+1,n):
    x=a[i]*a[j]
    l.append(x)
  b=[]
  for k in range(len(l)):
   s=l[k]
   b.append(sod(s))
  print(max(b))    
