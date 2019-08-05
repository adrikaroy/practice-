l=[0]
for i in range(0,16):
    l.append(pow(2,i))
    l.append(pow(3,i))

n=int(input())

print(l[n])

