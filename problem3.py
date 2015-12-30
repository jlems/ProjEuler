"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
import math

#this will hold my prime numbers
primeList = []
def largestPrime(x):
	#given x, only check non-even ints greater than 2 and less than
	#square root of x.

	
	#this will hold the other term to start the factorization process
	secondTerm = 0
	
	# first check if x is even
	if (x % 2 == 0):
		secondTerm = x / 2
		while(isPrime(secondTerm) == False):
			




def isPrime(x):

	upperBound = math.sqrt(x)
	intUpperBound = int(upperBound)

	#first check if 2 divides x, if it does, return
	if(x % 2 == 0):
		return
	for i in range(3,intUpperBound):
		#exclude evens
		if(i % 2 != 0):
			if(x % i == 0):
				print "here"
				return
	#if we get here, then x must be prime
	primeList.append(x)
	print primeList

isPrime(5234320)
	

