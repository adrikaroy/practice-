
s=input()
d=[0]*10
for i in s:
    if i.isalpha()==False:
        d[int(i)]+=1
print(*d)



