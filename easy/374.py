"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:
- -1: Your guess is higher than the number I picked (i.e. num > pick).
- 1: Your guess is lower than the number I picked (i.e. num < pick).
- 0: Your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.
"""


# region Solution

def guess(num: int) -> int:
    return 1


def guess_number(n: int) -> int:
    def binary_search(start: int, end: int) -> int:
        middle_num = start + ((end - start) // 2)
        num_guess = guess(middle_num)

        if num_guess == -1:
            return binary_search(start, middle_num - 1)
        elif num_guess == 1:
            return binary_search(middle_num + 1, end)
        else:
            return middle_num

    return binary_search(1, n)


# endregion

# region Tests

# 6
print(guess_number(10))

# 1
print(guess_number(1))

# 2
print(guess_number(2))

# endregion
