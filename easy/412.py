"""
Given an integer n, return a string array answer (1-indexed) where:
- answer[i] == "FizzBuzz" if "i" is divisible by 3 and 5.
- answer[i] == "Fizz" if "i" is divisible by 3.
- answer[i] == "Buzz" if "i" is divisible by 5.
- answer[i] == "i" (as a string) if none of the above conditions are true.
"""
from typing import List


# region Solution

def fizz_buzz(n: int) -> List[str]:
    results = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))

    return results


# endregion

# region Tests

# ["1", "2", "Fizz"]
print(fizz_buzz(3))

# ["1", "2", "Fizz", "4", "Buzz"]
print(fizz_buzz(5))

# ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
print(fizz_buzz(15))

# endregion
