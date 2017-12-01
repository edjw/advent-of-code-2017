from aocinput import aocinput

inpt = aocinput(1)
# inpt = '91212129'

# converts into a list of tuples where first element in tuple is the index
# and second element is main data
inpt = list(enumerate(inpt))

# matching numbers go in this list
matching_numbers = []

# matching numbers will be added up here
answer = 0

for digit in inpt:
    current_index = digit[0]
    next_index = current_index + 1

    if current_index == inpt[-1][0]: # if the last one
        if inpt[-1][1] == inpt[0][1]: # and if the last number matches the first one
            matching_numbers.append(inpt[-1][1]) # append that number to the matching_numbers list

    elif inpt[current_index][1] == inpt[next_index][1]:
        # if not the last one
        # and the number matches the next number in the list
        matching_numbers.append(inpt[current_index][1]) # append to list

for number in matching_numbers:
    answer += int(number)

print(answer)
