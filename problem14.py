# -*- coding: utf-8 -*-


"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all 
starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""




#biggestCount is used to keep track of the longest collatz sequence thus far
biggestCount = 0
tempCount = 1
def calc_longest():
	global biggestCount
	global tempCount
	finalNumber = 0
	for i in range(1,1000000):
		#print tempCount
		#print i
		collatz(i)
		#print "collatz is returning" + str(collatz(i))
		if(tempCount > biggestCount):
			
			biggestCount = tempCount
			finalNumber = i
		#print "\t" + str(biggestCount)
		tempCount = 1
	return finalNumber
		

def collatz(n):
	
	global tempCount
	#print n
	if (n == 1):
		#print "tempCount is " + str(tempCount)
		return tempCount
		
	
	elif (n % 2 == 0):
		#n = n / 2
		tempCount = tempCount + 1
		collatz(n/2)
		#if (n == 1):
		#	return tempCount
	
	else:
		#n = 3*n + 1
		tempCount = tempCount + 1
		collatz(3*n+1)
		#if (n == 1):
		#	return tempCount
	#return tempCount

#print calc_longest()

#print collatz(13)
print calc_longest()
