k=int(input())

for i in range(k):
    for j in range(i+1):
        if j==i:
            print(i+1,"",end="")
        else:    
            print(str(i+1)+"*",end="")
    print()
    
for i in range(k,0,-1):
    for j in range(i,0,-1):
        if j==1 :
            print(i,"",end="")
        else:    
            print(str(i)+"*",end="")
    print()
