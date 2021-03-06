
# 
# Project Euler problem 2
# Copyright (c) Project anaghajoshi. All rights reserved.
#  
# https://github.com/anaghajoshi/projecteuler
# 

"""
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""

# 
def add_even_fibonacci():
	#
	x = 1
	y = 2
	sum = 0	

	while x <= 4000000:

		if (x%2 ==0):
			sum += x
		x , y = y , x + y
			
	return sum


if __name__ == "__main__":
	print(add_even_fibonacci())