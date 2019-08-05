
a=[str(x) for x in input().split()]

s="".join(a)

i=int(s)+1

l=list(str(i))

"""
for x in range(len(l)):
    print(l[x],end=" ")
"""

print(*l)
