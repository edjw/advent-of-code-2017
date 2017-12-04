new_file = []
counter = 0

with open('input/4.txt', 'r') as f:
    for line in f:
        line = line.split() # makes a list out of the current string line, removes tabs and \n
        line = list(line) # makes the line a list
        new_file.append(line) # appends the line list to a fresh list ## not sure why I need this tbh

for line in new_file:
    if len(line) == len(set(line)):
    # if items in line is same as number of items in line with duplicates removed
        counter += 1
        # then add 1 to counter
print(counter)