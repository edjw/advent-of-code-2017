target = 347991
bottom_right_number = 1
previous_bottom_right_number = 1
row_column = 0
length_of_side = 0

while bottom_right_number < target:
    row_column += 1
    previous_bottom_right_number = bottom_right_number
    bottom_right_number = (row_column * 8) + previous_bottom_right_number # this is the key bit
    length_of_side = row_column * 2


nearest_corner = bottom_right_number

while (nearest_corner - length_of_side) >= target:
    nearest_corner -= length_of_side


middle_of_side = nearest_corner - (length_of_side // 2)

distance_to_middle_of_side = target - middle_of_side

distance_to_square_one = distance_to_middle_of_side + row_column


print("The target is {}.".format(target))
print("The bottom right number is {}.".format(bottom_right_number))
print("The row/column of the bottom right number is {}.".format(row_column))
print("The length of a side is {}.".format(length_of_side))
print("The nearest corner is {}.".format(nearest_corner))
print("The distance to middle of the side is {}.".format(distance_to_middle_of_side))
print("The distance to square one is {}.".upper().format(distance_to_square_one))
