"""
Multiples of 3 and 5
Problem 1

https://projecteuler.net/problem=1

Tue Jan 20 20:09:24 2015

If we list all the natural numbers below 10 that are 
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum 
of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

container = []
highest_value = 1000

def get_multiples(multiple, highest_value):

	for i in range(0, highest_value, multiple):
		if i != 0:
			print "Adding %s to the list." % (i)
			container.append(i)

# Remove duplicates
def remove_duplicates(values):
	output = []
	seen = set()
	for x in values:
		if x not in seen:
			output.append(x)
			seen.add(x)
	return output

get_multiples(3, highest_value)
get_multiples(5, highest_value)
result = remove_duplicates(container)

print container

print "Result %s" % sum(result)