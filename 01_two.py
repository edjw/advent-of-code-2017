from aocinput import aocinput

inpt = aocinput(1)
# inpt = '12131415'
length = int(len(inpt))
half_length = int(len(inpt) / 2)

# converts into a list of tuples where first element in tuple is the index
# and second element is main data
inpt = list(enumerate(inpt))

# matching numbers go in this list
matching_numbers = []

# matching numbers will be added up here
answer = 0

for digit in inpt:
    current_index = digit[0]

    if current_index + half_length < length:
        next_index = current_index + half_length
        if inpt[current_index][1] == inpt[next_index][1]:
            matching_numbers.append(inpt[current_index][1])
    elif current_index + half_length >= length:
        next_index = current_index - half_length
        if inpt[current_index][1] == inpt[next_index][1]:
            matching_numbers.append(inpt[current_index][1])

for number in matching_numbers:
    answer += int(number)

print(answer)
