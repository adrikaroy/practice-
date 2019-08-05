"""
a = [1,2,3,4,5,6,7,8,9,10]
q=3
l=1,r=4
l=2,r=5
l=7,r=10


n,q=map(int, input().split())

a=list(map(int, input().split()))

for i in range(q):
	l,r=map(int,input().split())
	s=0
	for j in range(l,r+1):
		s+=a[j-1]
	print(s)		
"""

n,q=map(int, input().split())

a=list(map(int, input().split()))

m=[0]
s=0
for i in a:
	s=s+i
	m.append(s)

for i in range(q):
	l,r=map(int,input().split())

	print(m[r]-m[l-1])






















