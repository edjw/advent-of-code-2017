from itertools import combinations

new_file = []
number_of_passphrases = 0 #lines
lines_containing_anagrams = []
number_of_passphrases_containing_anagrams = 0

with open('input/4.txt', 'r') as f:
    for line in f:
        line = line.split() # makes a list out of the current string line, removes tabs and \n
        line = list(line) # makes the line a list
        new_file.append(line) # appends the line list to a fresh list ## not sure why I need this tbh

for line in new_file:
    number_of_passphrases +=1 # counts the number of lines
    sorted_line_list = []

    for word in line:
        word = ''.join(sorted(word))
        sorted_line_list.append(word)

    all_permutations_sorted_line_list = list(combinations(sorted_line_list, 2))

    for pairing in all_permutations_sorted_line_list:
        if pairing[0] == pairing[1]:
            lines_containing_anagrams.append(line)
            number_of_passphrases_containing_anagrams += 1
            break

print(number_of_passphrases - number_of_passphrases_containing_anagrams)
