t=int(input())
for i in range(t):
 n=int(input())
 s=input()
 l=["a","e","i","o","u"]
 c=0
 for i in range(len(s)):
  if i != 0:
   if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
    if s[i-1] not in l:
     c+=1
 print(c)   
          
