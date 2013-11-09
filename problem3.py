#!/usr/bin/python

import math

numb = 600851475143
#numb = 600851475143
rank = 0


def primes(n):
	n = int(math.sqrt(n))
	if n<=2:
		return []
	sieve=[True]*(n+1)
	for x in range(3,int(n**0.5)+1,2):
	    for y in range(3,(n//x)+1,2):
	        sieve[(x*y)]=False
	return [2]+[i for i in range(3,n,2) if sieve[i]]

def primes_op(n):
	factor = 2
	lastFactor = 1
	n = int(math.sqrt(n))
	if n % 2 == 0:
		lastFactor = factor
		n = n / 2
		while n % 2 == 0:
			n = n / 2

	factor = 3
	while n > 1:
		if n % factor == 0:
			lastFactor = factor
			n = n / factor
			while n % factor == 0:
				n = n / factor
			factor += 2

	print(lastFactor)

a = primes(numb)

for i in a:
	if numb % i == 0:
		print i 


#primes_op(numb)

# 6857