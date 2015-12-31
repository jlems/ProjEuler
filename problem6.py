"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

import math

def tenThousandFirstPrime():
	counter = 0
	#start with 3 as the first prime number
	primeGuess = 3
	while(counter < 10000):
		
		#only increment the counter if the number is prime. Also increment primeGuess by 2
		#since evens are not prime
		if(isPrime(primeGuess)):
			counter = counter + 1
			primeGuess = primeGuess + 2
			
		else:
			primeGuess = primeGuess + 2
	
	return primeGuess



def isPrime(x):
	if(x % 2 == 0):
		return False
	
	upperBound = math.sqrt(x)
	intUpperBound = int(upperBound)
	
	
	
	for i in range(3, intUpperBound + 1):
		if(x % i == 0):
			
			return False
	print x
	return True


tenThousandFirstPrime()
