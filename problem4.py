
def poli1():
	rank = 0

	for i in range(999, 100, -1):
		for j in range(999, i, -1):
			k = str(i*j)
			if k == k[::-1]:
				if int(k) > 900000: print int(k)
				break

poli1()

# 906609
