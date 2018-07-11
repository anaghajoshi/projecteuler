
# 
# Project Euler problem 3
# Copyright (c) Project anaghajoshi. All rights reserved.
#  
# https://github.com/anaghajoshi/projecteuler
# 

"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# 
def is_prime(x):
    if x < 2:
        return False
    else:
        if x == 2:
            return True
        else:
            for i in range(2, x):
                if x % i == 0:
                    return False
            return True


def largest_prime_factor(num):
	#
	factors_list = [i for i in range(1,num) if num%i == 0 and is_prime(i)]

	return max(factors_list)


if __name__ == "__main__":
	num = input("Enter the number: ")
	print(largest_prime_factor(int(num)))