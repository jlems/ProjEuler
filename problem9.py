"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for 
which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

def findProduct():
	
	#iterate through all triplets from 1 to 500
	for i in range(1,501):
		for j in range(1,501):
			for k in range(1,501):
				#square each term to test for 
				#pythagorean trips
				isq = i*i
				jsq = j*j
				ksq = k*k
				if((isq + jsq) == ksq):
					#check for sum condition
					if((i + j + k) == 1000):
						return (i * j * k)
						
print findProduct()
