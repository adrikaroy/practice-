t=int(input())
for j in range(t):
 s=list(map(str,input().split()))
 c=0
 for i in s:
  if i=="not":
   c+=1
 if c>0: 
  print("Real Fancy")
 else:
  print("regularly fancy")
