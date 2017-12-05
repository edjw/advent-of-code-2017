counter = 0

with open('input/5.txt', 'r') as f:

    # list comprehension to make single list of all numbers in file
    all_numbers = [line.strip() for line in f]

    # enumerate makes list of tuples with structure of (index, item)
    all_numbers_tuples = enumerate(all_numbers)

    # making the list of tuples into a list of lists so they can be changed
    all_numbers = [list(tpl) for tpl in all_numbers_tuples]

    # the index of last number for higher outer boundary
    last_number_index = all_numbers[-1][0]

    # current index. Need this so while loop starts
    current_number_index = all_numbers[0][0]

    # while the index of the number is still inside the range of the list
    while current_number_index >= 0 and current_number_index <= last_number_index:

        # count number of jumps
        counter += 1

        # set the current number as the number linked to current index
        current_number = int(all_numbers[current_number_index][1])

        if current_number >= 3:
            # replace the current number in the list with the current number minus 1
            all_numbers[current_number_index][1] = current_number - 1
        else:
            # replace the current number in the list with the current number plus 1
            all_numbers[current_number_index][1] = current_number + 1

        # move the current index to the current index plus the current number
        current_number_index = all_numbers[current_number_index][0] + current_number

print("That took {} steps.".format(counter))
