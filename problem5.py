"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""


def smallestMultiple():

	count = 0
	#loop over numbers from 0 to a very large number, at 20 unit steps. 
	for i in range(0, 1000000000, 20):
		#must only check numbers greater than 0 since everything is a multiple of 0
		if(i > 0):
			count = 0
			# now check every number starting from 3 all the way up to 19
			for j in range(3, 20):
				#if no remainder when j | i, then enter if statement and increment count
				if(i % j == 0):
					count = count + 1
					#if we reach here then we have hit every number from 1 to 20
					if(count == 17):
						return i
				#if there is a reaminder, break out of inner for loop and try the next number
				else:
					break
	#get here only if no number was found, so increase the range
	return -1
	

print smallestMultiple()
