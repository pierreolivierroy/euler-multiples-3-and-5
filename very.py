
#!/usr/bin/python

numbers = []
n = 1000

for i in xrange(1, n):
	if (i % 3) == 0 or (i % 5) == 0:
		numbers.append(i)
print sum(numbers)