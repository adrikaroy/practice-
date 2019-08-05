"""
t=int(input())
for i in range(t):
 n,k=map(int, input().split())
 a=list(map(int,input().split()))
 s=sorted(a)
 l=0
 u=len(s)-1
 c=0
 while(l<u):
  if s[l]+s[u]==k:
   c=c+1
   break
  elif s[l]+s[u]<k:
   l=l+1
  else:
   u=u-1
 if(c==0):
  print("No")
 else:
  print("Yes")   

t=int(input())
for i in range(t):
 p=int(input())
 l=list(map(int,input().split()))
 s=sorted(l,reverse=True)
 b=min(s[0],s[1])
 if ((b-1)>(p-2)):
     print(p-2)
 else:
     print(b-1)



t=int(input())
for i in  range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    l=[]
    c=[]
    for j in range(len(a)):
        if j==0:
            s=a[j+1]+a[n-1]
            l.append(s)
        elif j==(n-1):
            s=a[j-1]+a[0]
            l.append(s)
        else:    
            s=a[j+1]+a[j-1]
            l.append(s)

    for j in range(len(l)):
        if l[j]<b[j]:
            c.append(b[j])
    
    f=sorted(c,reverse=True)
    if (len(f))==0:
        print(-1)
    else:
        print(f[0])




t=int(input())
for k in range(t):
    r,c=map(int,input().split())
    l=[]
    f=0
    for i in range(r):
        a=list(map(int,input().split()))
        l.append(a)
    for i in range(r):
        for j in range(c):
            if((i==0)and(j==0))or((i==r-1)and(j==c-1))or((i==0)and(j==c-1))or((i==r-1)and(j==0)):
                #print("first if",i,j)
                if (l[i][j]>2):
                    f+=1
            elif ((i==0)and(j>0 and j<c-1)) or ((j==0)and(i>0 and i<r-1)) or ((i==r-1)and(j>0 and j<c-1)) or ((j==c-1) and (i>0 and i<r-1)):
                #print("first elif",i,j)
                if(l[i][j]>3):
                    f=f+1 
            elif (i>0 and j>0 and i<r-1 and j<c-1):
                #print("sec if",i,j)
                if(l[i][j]>4):
                    f=f+1 
    if f>0:
        print("Unstable")
    else:
        print("Stable")


t=int(input())
for k in range(t):
    r,c=map(int,input().split())
    l=[]
    f=0
    for i in range(r):
        a=list(map(int,input().split()))
        l.append(a)
    for i in range(r):
        for j in range(c):
            if((i==0)and(j==0))or((i==r-1)and(j==c-1))or((i==0)and(j==c-1))or((i==r-1)and(j==0)):
                if (l[i][j]>2):
                    f+=1
            elif (i==0 or i==r-1 or j==0 or j==c-1):
                if(l[i][j]>3):
                    f=f+1 
            else:
                if(l[i][j]>4):
                    f=f+1 
    if f>0:
        print("Unstable")
    else:
        print("Stable")

"""

t=int(input())
for i in range(t):
 n=int(input())
 l=list(map(int,input().split()))
 a=[]
 s=sum(l)
 for j in range(n):
  if((n-1)*s == n*(s-l[j])):
   a.append(l[j])
 if(len(a)==0):
  print("Impossible")
 else: 
  print(min(a))

































































