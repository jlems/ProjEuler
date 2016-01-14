"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

import math

primesList = [2]
count = 0
def findSum():
	for i in range(2, 2000000):
		isPrime(i)

	finalSum = sum(primesList)
	return finalSum


def isPrime(x):
	
	#idea here is to divide x by each number from 3 to the square root of x. 
	#if any of those numbers in that range divide x evenly, then we know
	#that x is not prime
	upperBound = math.sqrt(x)
	intUpperBound = int(upperBound)
	#check if x is prime
	if(x % 2 == 0):
		return False
	for i in range(3, intUpperBound + 1):
		if(x % i == 0):
			return False
	primesList.append(x)
print findSum()
