#!/usr/bin/python

def col(n, c):
	while n != 1:
		if n**0.5 
		if n % 2 == 0:
			n /= 2
			c += 1
		else:
			n = 3*n + 1
			c += 1
	return c

m = 0
n = 0

for i in xrange(2, 1000001):
	t = col(i, 1)
	if m < t:
		m = t
		n = i

print(n)