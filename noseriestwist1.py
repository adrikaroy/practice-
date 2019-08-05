def series(n):
	if n%2==0:
		x=n//2
		print(6*(x-1))
	else:
		x=n//2
		print(7*(x))	

n=int(input())
series(n)


#0,0,7,6,14,12,21,18, 28,......
