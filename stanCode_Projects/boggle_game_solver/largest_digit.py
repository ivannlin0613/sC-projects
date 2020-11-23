"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""

# for storing the largest digit of the number
maxmm = 0


def main():
	global maxmm
	print(find_largest_digit(12345))      # 5
	maxmm = 0
	print(find_largest_digit(281))        # 8
	maxmm = 0
	print(find_largest_digit(6))          # 6
	maxmm = 0
	print(find_largest_digit(-111))       # 1
	maxmm = 0
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, numbers which were offered to find out the largest digit
	:return: int, the largest digit among n
	"""
	# turn n into positive number
	n = abs(n)
	global maxmm
	# Base case!
	if n == 0:
		pass
	else:
		# the last digit of the number
		digit1 = n%10
		if digit1 > maxmm:
			maxmm = digit1
		new_n = n//10

		if new_n != 0:
			find_largest_digit(new_n)
			return maxmm
		# for the case of only one digit of number
		else:
			return digit1


if __name__ == '__main__':
	main()
