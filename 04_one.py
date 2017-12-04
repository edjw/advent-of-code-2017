counter = 0

with open('input/4.txt', 'r') as f:
    for line in f:
        line = line.strip().split() # strip removes tabs and \n. split makes a list out of the current string line
        if len(line) == len(set(line)):
            counter += 1
print(counter)