def primes(n):
	if n<=2:
		return []
	sieve=[True]*(n+1)
	for x in range(3,int(n**0.5)+1,2):
		if sieve[x]:
		    for y in range(3,(n//x)+1,2):
		        sieve[(x*y)]=False
	return [2]+[i for i in range(3,n,2) if sieve[i]]

print sum(primes(2*(10**7)))

# 142913828922