from itertools import permutations

new_file = []
number_of_passphrases = 0 #lines
number_of_passphrases_containing_anagrams = 0 #lines containing anagrams

with open('input/4.txt', 'r') as f:
    for line in f:
        line = line.split() # makes a list out of the current string line, removes tabs and \n
        line = list(line) # makes the line a list
        new_file.append(line) # appends the line list to a fresh list ## not sure why I need this tbh

for line in new_file:
    number_of_passphrases += 1 # counts the number of lines
    sorted_line_list = []

    for word in line:
        word = ''.join(sorted(word)) # sorts each word in the line alphabetically
        sorted_line_list.append(word) # adds the sorted words into a fresh list

    all_permutations_sorted_line_list = list(permutations(sorted_line_list, 2)) # makes a list of all permutations of the sorted list

    for pairing in all_permutations_sorted_line_list:
        if pairing[0] == pairing[1]: # if the words match then there's an anagram
            number_of_passphrases_containing_anagrams += 1 # count that there's a matched word
            break # break so it only counts the first match of each line

print(number_of_passphrases - number_of_passphrases_containing_anagrams)
