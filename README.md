# Advent of Code 2017

My work on the [Advent of Code 2017](https://adventofcode.com/2017). I don't think code quality will be all that great!

## Day 1

[Part One](https://github.com/edjw/advent-of-code-2017/blob/master/one_one.py)

```
...Review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

For example:

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.

1111 produces 4 because each digit (all 1) matches the next.

1234 produces 0 because no digit matches the next.

91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

What is the solution to your captcha?
```

[Part Two](https://github.com/edjw/advent-of-code-2017/blob/master/one_two.py)

```
Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.

1221 produces 0, because every comparison is between a 1 and a 2.

123425 produces 4, because both 2s match each other, but no other digit has a match.

123123 produces 12.

12131415 produces 4.

```

## Day 2

[Part One](https://github.com/edjw/advent-of-code-2017/blob/master/two_one.py)

```
The spreadsheet consists of rows of apparently-random numbers.
To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum.
For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8

The first row's largest and smallest values are 9 and 1, and their difference is 8.

The second row's largest and smallest values are 7 and 3, and their difference is 4.

The third row's difference is 6.

In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?
```

<!-- [ --> Part Two
<!-- ](https://github.com/edjw/advent-of-code-2017/blob/master/two_two.py) -->

```
It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number.

They would like you to find those numbers on each line, divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5

    In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
    In the second row, the two numbers are 9 and 3; the result is 3.
    In the third row, the result is 2.

In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?

```