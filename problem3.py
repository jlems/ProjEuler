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
	temp = 1
	while (temp > 0):
		print temp
		temp = x / 2.0
		#if(temp % 2 == 0):
		#	print "in the if"
		if(isPrime(temp)):
			return temp
		else:
			x = x - 1
				#temp = temp - 1
		#else:
		#	x = x - 1
			#temp = temp - 1




def isPrime(x):

	upperBound = math.sqrt(x)
	intUpperBound = int(upperBound)

	#first check if 2 divides x, if it does, return
	if(x % 2 == 0):
		return False
	for i in range(3,intUpperBound + 1):
		#exclude evens
		if(i % 2 != 0):
			if(x % i == 0):
				print "here"
				return False
	#if we get here, then x must be prime
	return True
	primeList.append(x)
	print primeList

print largestPrime(15)


