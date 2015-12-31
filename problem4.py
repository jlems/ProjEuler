#coding=utf-8
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit 
numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""



def largestPalindrome():
	largestPal = 0
	for i in range(100, 1000):
		for j in range(100, 1000):
			product = i * j
			if(isPalindrome(product)):
				if(product > largestPal):
					largestPal = product
				#print largestPal
	return largestPal



def isPalindrome(x):
	#string the x and reverse it
	stringedPal = str(x)[::-1]
	
	#check if the reversed string matches the orgianl string
	if (stringedPal== str(x)):
		return True
		
	else:
		return False


print largestPalindrome()
