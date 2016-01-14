"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

#get the value of 2**1000 and str it and store it in the variable temp
temp = str(2**1000)
tempList = []

#in tempList, iterate over the string temp and append each element of temp to 
#the tempList, making sure to convert it to an integer so that the list is a list
# of ints
for i in temp:
	tempList.append(int(i))
#sum the tempList
print sum(tempList)

