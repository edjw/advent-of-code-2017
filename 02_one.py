from re import sub

total_difference = 0

with open('input/2.txt', 'r') as f:
    for line in f:
        line = sub('\t', " ", line) # removing the tabs between the numbers
        line = sub('\n', "", line) # removing the \n at the end of each line
        line = line.split() # makes a list out of the current string line

        # makes each item in the list an integer
        # otherwise max(line) matches 858 for 1st line as 8 is highest first digit in the line
        line = list(map(int, line))

        largest = max(line)
        smallest = min(line)
        difference = largest - smallest
        total_difference += difference
print(total_difference)
