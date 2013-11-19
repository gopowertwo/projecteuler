sums = 0
sqsum = 0
n = 10**100000

# for i in range(n+1):
# 	sums += i*i
# 	sqsum += i

sqsum1 = n*(n+1)/2
sums1 = (2*n+1)*(n+1)*n/6

print sqsum**2 - sums
print sqsum1**2 - sums1

# 25164150