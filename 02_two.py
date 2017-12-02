from re import sub
from itertools import permutations

total_difference = 0

with open('input/2.txt', 'r') as f:
    for line in f:
        line = sub('\t', " ", line) # removing the tabs between the numbers
        line = sub('\n', "", line) # removing the \n at the end of each line
        line = line.split() # makes a list out of the current string line

        # makes each item in the list an integer
        # otherwise max(line) matches 858 for 1st line as 8 is highest first digit in the line
        line = list(map(int, line))

        line = list(permutations(line, 2)) # makes list of tuples containing all possible pairings of two numbers in the line

        for pairing in line:
            if pairing[0] == pairing[1]: # pass if the numbers are the same; would leave 0 in next elif
                pass
            elif pairing[0] % pairing[1] == 0: # if 1st num divided by 2nd num is 0 then they're even
                difference = pairing[0] // pairing[1] # divide 1st num by 2nd numb
                total_difference += difference # add the difference to the total
            else: # otherwise the numbers don't evenly divide
                pass
print(total_difference)
