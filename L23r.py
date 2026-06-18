'''
    LIMITED SUM

    Your task is to implement a function limited_sum(values, limit) that
    returns the maximum sum of a subset of values such that the sum is
    less than or equal to limit. The values and limit are assumed to be 
    non-negative integers. E.g., for values = [7, 5, 13, 11, 19] and limit = 28, 
    the largest sum less than or equal to the limit is 26 = 7 + 19.

    Input:  The first line contains a Python list values with at most 100 
            non-negative integers. The second line contains a non-negative
            integer limit <= 20_000.

    Output: The result of calling limited_sum(values, limit).

    Example:

      Input:  [7, 5, 13, 11, 19]
              28

      Output: 26

    Note: The below code already handles reading the input and printing
          the result of calling limited_sum(values, limit).
'''


def limited_sum(values, limit):
    # insert code
    pass
#> validate input
    assert isinstance(values, list)
    assert all(isinstance(value, int) for value in values)
    assert all(0 <= value <= 1000 for value in values)
    assert 1 <= len(values) <= 100
    assert isinstance(limit, int)
    assert 0 <= limit <= 20_000
#< validate input
#> solution
    from functools import cache
    @cache
    def solve(k, limit):
        if k == 0:
            return 0
        if values[k - 1] > limit:
            return solve(k - 1, limit)
        return max(solve(k - 1, limit), values[k - 1] + solve(k - 1, limit - values[k - 1]))
    return solve(len(values), limit)
#< solution


values = eval(input())
limit = int(input())
print(limited_sum(values, limit))
