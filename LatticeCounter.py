import math

#It's a fact of combinatorics that this lattice problem is given by 2*n choose n
#where n is the number of sides of the square lattice.
def lattice_counter(n):
		return math.factorial(2*n) / (math.factorial(n)*math.factorial(2*n - n))
print lattice_counter(20);
