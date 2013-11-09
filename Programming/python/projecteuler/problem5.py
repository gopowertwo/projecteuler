step = 2*3*5*7*11*13*17*19

for i in range(0, 10**10, step):
	if i % 20 == 0 and i % 18 == 0 and i % 16 == 0:
		print i
		break

# 232792560