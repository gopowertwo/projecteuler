#!/usr/bin/python

def fib1():
	sums = 0

	i = 1
	j = 1

	while j <= 4*(10**30000):
		j = i + j
		i = j - i
		if(j % 2 == 0):
			sums += j

	print(sums)

def fib2():
	sums = 0
	i = 1
	j = 1
	h = i + j

	while h <= 4*(10**30000):
		sums += h
		i = h + j
		j = i + h
		h = i + j

	print(sums)



#fib1()
fib2()