'''
    SIGNED SUBSET

    Your task is to write a function subset(values, n), that given
    a sorted list of distinct positive integers and an integer n,
    determines if there exists a subset of the values that has sum n,
    possibly by negating some of the values. E.g. subset([1, 5, 11, 17], 7)
    should return True, since 7 = 1 + -5 + 11 = 1 + -11 + 17.

    Input:  A single line with a Python expression calling subset,
            with len(values) <= 40, each value <= 1000, n <= 40000.

    Output: The result of evaluating the expression.

    Example:

      Input:  subset([1, 5, 11, 17], 7)

      Output: True

    Note: The below code already handles the input and output.
'''

#> solution
from functools import cache
#< solution

def subset(values, n):
    # insert code
    pass
#> validate input
    assert all(0 < value <= 1000 for value in values)
    assert values == sorted(values)
    assert len(values) == len(set(values)) <= 40
#< validate input
#> solution
    @cache
    def solve(i, n):
        if n == 0:
            return True
        if i == 0:
            return False
        return solve(i - 1, n) or solve(i - 1, n - values[i - 1]) or solve(i - 1, n + values[i - 1])

    return solve(len(values), n)
#< solution
#> show all solutions (not part of problem)
def all_subsets(values, n):
    @cache
    def solve(i, n):
        if n == 0:
            return [[]]
        if i == 0:
            return []
        return (
            solve(i - 1, n) +
            [[*sol,  values[i - 1]] for sol in solve(i - 1, n - values[i - 1])] +
            [[*sol, -values[i - 1]] for sol in solve(i - 1, n + values[i - 1])]
        )

    return solve(len(values), n)
#< 


print(eval(input()))
