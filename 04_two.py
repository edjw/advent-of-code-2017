from itertools import combinations

number_of_passphrases = 0 #lines
number_of_passphrases_containing_anagrams = 0 #lines containing anagrams

with open('input/4.txt', 'r') as f:
    for line in f:
        line = line.strip().split()
        # strip removes tabs and \n.
        #split makes a list out of the current string line

        number_of_passphrases += 1 # counts the number of lines
        sorted_line_list = []

        for word in line:
            word = ''.join(sorted(word)) # sorts each word in the line alphabetically
            sorted_line_list.append(word) # adds the sorted words into a fresh list

        all_combinations_sorted_line_list = list(combinations(sorted_line_list, 2))
        # makes a list of all combinations of the sorted list
        # slightly faster than permutations because will match quicker below

        for pairing in all_combinations_sorted_line_list:
            if pairing[0] == pairing[1]: # if the words match then there's an anagram
                number_of_passphrases_containing_anagrams += 1 # count that there's a matched word
                break # break so it only counts the first match of each line

number_of_passphrases_not_containing_anagrams = number_of_passphrases - number_of_passphrases_containing_anagrams

print("The number of valid passphrases (not containing anagrams) is {}.".format(number_of_passphrases_not_containing_anagrams))
