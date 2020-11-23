"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# list of all words in FILE
python_list = []


def main():
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    while True:
        s = input('Find anagrams for: ')
        if s == '-1':
            break
        else:
            read_dictionary()
            find_anagrams(s)


def read_dictionary():
    """
    Read in the FILE(dictionary.txt) and turn it into a bunch of vocabulary list

    :return: This function does not return anything
    """
    global python_list
    with open(FILE, 'r') as f:
        for line in f:
            # turn all vocabs into a list
            word = line.split()
            python_list += word


def find_anagrams(s):
    """
    This function helps find out whether the words inside the list(anagrams) is in python_list(FILE),
    and print out how many words were found and show all the existed anagrams in the form of list.

    :param s: str, the word which user typed in in order to find out all the anagrams among those characters
    """
    # list, all anagrams of s
    anagrams = []
    print('Searching...')
    find_anagrams_helper(s, [], anagrams)
    # list, existed anagrams in python_list
    chosen = []
    count = 0
    for i in range(len(anagrams)):
        if anagrams[i] in python_list and anagrams[i] not in chosen:
            count += 1
            print(f'Found: {anagrams[i]}')
            chosen.append(anagrams[i])
            print('Searching...')
    print(f'{count} anagrams: {chosen}')


def find_anagrams_helper(s, ans, anagrams):
    """
    Backtracking, find out all the anagrams of s and hold it in the list(anagrams)

    :param s: str, the word which user typed in in order to find out all the anagrams among those characters
    :param ans: []
    :param anagrams: []
    """
    # the container for joining a bunch of characters into a string
    permutations = ''

    # Base case
    if len(s) == 0:
        permutations = permutations.join(ans)
        anagrams.append(permutations)
    else:
        for i in range(len(s)):
            if len(s) != 0:
                ans.append(s[i])
                sub_s = ''.join(ans)
                # check whether prefix can be found in python_list
                if has_prefix(sub_s):
                    find_anagrams_helper(s[i+1:]+s[:i], ans, anagrams)
                    ans.pop()
                else:
                    ans.pop()


def has_prefix(sub_s):
    """
    :param sub_s: str, for finding whether this string is a prefix for the words in dictionary
    :return: bool
    """
    for word in python_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
