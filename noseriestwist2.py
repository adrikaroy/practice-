#1, 1, 2, 3, 4, 9, 8, 27, 16, 81, 32, 243, 64, 729, 128, 2187,..............

def series(n):
	if n%2==0:
		x=n//2
		print(pow(3,x-1))
	else:
		x=n//2
		print(pow(2,x))

n=int(input())
series(n)			