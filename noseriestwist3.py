#0, 0, 2, 1, 4, 2, 6, 3, 8, 4, 10, 5, 12, 6, 14, 7, 16, 8,...........

def series(n):
	if n%2==0:
		x=n//2
		print(x-1)
	else:
		x=n//2
		print(2*x)


t=int(input())
for _ in range(t):
	n=int(input())
	series(n)			