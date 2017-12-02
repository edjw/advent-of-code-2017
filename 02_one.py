total_difference = 0

with open('input/2.txt', 'r') as f:
    for line in f:
        line = line.split() # makes a list out of the current string line, removes tabs and \n

        # makes each item in the list an integer
        # otherwise max(line) matches 858 for 1st line as 8 is highest first digit in the line
        line = list(map(int, line))

        largest = max(line)
        smallest = min(line)
        difference = largest - smallest
        total_difference += difference
print(total_difference)
