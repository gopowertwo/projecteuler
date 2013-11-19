import math
from fractions import gcd

def pit1():
	for a in range(1,9999):
		for b in range(1,9999):
			c = 10000 - a - b
			if a*a + b*b == c*c:
				print a*b*c
				exit()

def pit2():
	s = 10000**2
	s2 = s / 2
	mlimit = int(math.sqrt(s))

	for m in range(2, mlimit):
		if s2 % m == 0:
			sm = s2 / m
			while sm % 2 == 0:
				sm = sm / 2
			if m % 2 == 1:
				k = m + 2
			else:
				k = m + 1
			while k < 2*m and k <= sm:
				if sm % k == 0 and gcd(k, m) == 1:
					d = s2 / k*m
					n = k - m 
					a = d*(m*m - n*n)
					b = 2*d*m*n
					c = d*(m*m + n*n) 
					print(a*b*c)
				k += 2

# pit1()
# pit2()
if math.sqrt(10**2000) == (10**2000)**0.5:
	print("Hey");
# 31875000