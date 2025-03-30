"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the sum of the squares of its digits.
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or loops endlessly in a cycle which does not
  include 1.
- Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""


# region Solution

def is_happy(n: int) -> bool:
    square_sums_set = set()

    current_square_sum = 0
    while current_square_sum != 1:
        current_square_sum = 0

        while n != 0:
            current_digit = n % 10
            n = int(n / 10)

            current_square_sum += (current_digit * current_digit)

        if current_square_sum in square_sums_set:
            return False
        else:
            square_sums_set.add(current_square_sum)

        n = current_square_sum

    return True


# endregion

# region Tests

# True
print(is_happy(19))

# False
print(is_happy(2))

# endregion
