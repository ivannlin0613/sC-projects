"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# List for storing words in FILE
dict_list = []

# Boggle board
boggle_board = []

# Neighbor coordinates
neighbors = [(-1, -1), (0, -1), (1, -1),  (-1, 0),       (1, 0),  (-1, 1), (0, 1), (1, 1)]

# To prevent same combination of words being printed out
# and calculate how many words being found
words_found = []


def main():
	"""
	This program first requires user to type in 4 row of letters, and it will help find
	the existed word combinations which has four characters or more among those letters.
	"""
	read_dictionary()
	user_input()
	letter_input_machine()


def letter_input_machine():
	"""
	This function walks through the boggle board and send each letter as the starter
	for words_finder to find out the matching words.
	"""
	for y in range(len(boggle_board)):
		for x in range(len(boggle_board[y])):
			words_finder(boggle_board[y][x], y, x, [(y, x)])
	if len(words_found) != 0:
		print(f'There are {len(words_found)} words in total.')


def words_finder(word, y, x, used_coord):
	"""
	This function receives the letter from letter_input_machine, it's coordinates and a list of visited coordinates
	and find out all the word combinations from the starter letter(word).
	"""
	global words_found
	# check whether words in dict_list uses {word} as its prefix
	if len(word) >= 3 and not has_prefix(word):
		return
	if word in dict_list and len(word) >= 4 and word not in words_found:
		words_found.append(word)
		print(f'Found \"{word}\"')

	# keep looping new coordinates to find new character combinations
	for dx, dy in neighbors:
		new_x = x+dx
		new_y = y+dy
		if (new_y, new_x) not in used_coord and is_in_board(new_x, new_y):
			used_coord.append((new_y, new_x))
			words_finder(word+boggle_board[new_y][new_x], new_y, new_x, used_coord)
			used_coord.remove((new_y, new_x))


def is_in_board(nx, ny):
	"""
	This function makes sure the new coordinates is in the board
	"""
	if 0 <= nx < len(boggle_board) and 0 <= ny < len(boggle_board):
		return True
	else:
		return False


def user_input():
	"""
	This function asks user to fill in each row of the boggle board
	"""
	is_correct = False
	while not is_correct:
		row_1 = input('1 row of letters: ').lower()
		if len(row_1) == 7:
			row_2 = input('2 row of letters: ').lower()
			if len(row_2) == 7:
				row_3 = input('3 row of letters: ').lower()
				if len(row_3) == 7:
					row_4 = input('4 row of letters: ').lower()
					if len(row_4) == 7:
						is_correct = True
						bogl_board(row_1, row_2, row_3, row_4)
					else:
						print('Illegal format')
						is_correct = True
				else:
					print('Illegal format')
					is_correct = True
			else:
				print('Illegal format')
				is_correct = True
		else:
			print('Illegal format')
			is_correct = True


def bogl_board(r1, r2, r3, r4):
	"""
	Turn each row of user typed in letters into individual letter list
	This function does not return anything
	"""
	global boggle_board
	str1 = ''.join(r1.split())
	str2 = ''.join(r2.split())
	str3 = ''.join(r3.split())
	str4 = ''.join(r4.split())
	boggle_board.append(str1)
	boggle_board.append(str2)
	boggle_board.append(str3)
	boggle_board.append(str4)


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dict_list
	with open(FILE, 'r') as f:
		for line in f:
			word = line.split()
			# delete unnecessary words for word prefix search
			if len(word[0]) >= 4:
				dict_list += word


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict_list:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
