"""
	Multiples of 3 and 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.


"""
#this function finds the multiples of 3 and 5 and 
#returns the sum of all those numbers.
# x is the number which we cannot go above (ceiling)
def solve(x):
	# make a list to contain the multiples of 3 and 5
	sumList = []
	# this will contain the sum of the multiples
	finalSum = 0

	#find all the multiples of 3 and 5 below x
	for i in range(x):
		if(i >= 3):
			if(i % 3 == 0 or i % 5 == 0):
				sumList.append(i)

	finalSum = sum(sumList)

	return finalSum


print solve(1000)
