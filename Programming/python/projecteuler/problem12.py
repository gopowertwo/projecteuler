#!/usr/bin/python

import itertools 

def powerset(iterable):
    s = list(iterable)
    return (itertools.combinations(s, r) for r in range(len(s)+1)]

def genFactors(n):
	"""Generate the factors of an integer."""
	yield 1
	for i in xrange(2, n/2 + 1):
		if n % i == 0:
			yield i
	yield n

def factors(n):
	"""Return the factors of a integer."""
	return list(genFactors(n))


def divs(n):
	l = factors(n)
	l = powerset(l)
	res = []
	for i in l:
		prod = 1
		for s in i:
			prod *= s
		res += [s]

	return res


print(powerset([1,2,3]))

sum = 0
i = 0

while(True):

	i += 1
	sum += i
	break

