#!/usr/bin/python

def sum1():
		sums = 0

		for i in range(10000000 + 1):
				if(i % 3 == 0 or i % 5 == 0):
					sums += i
		print(sums)

def sum2(n):

		sums = 3*sum(range(n // 3 + 1)) + 5*sum(range(n // 5 + 1)) - 15*sum(range( n // 15 + 1))
		print(sums)

#sum2(10000000)
sum1()
