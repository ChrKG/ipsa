'''
    ZEROSUM

    Given a list of integers, find three integers in the list that sum to zero.

    Input:  A single line with n distinct integers separated by spaces, where
            3 <= n <= 5000 and each integer is in the range -10**10 to 10**10.
            It is guaranteed that the input contains a unique solution, i.e., 
            three exist integers x < y < z in the list such that x + y + z = 0.

    Output: A single line with the three integers that sum to zero, 
            separated by spaces and in increasing order.

    Example:

      Input:  -67 3 -11 -93 -32 7 9 -36 53 -12

      Output: -12 3 9
'''


# insert code
pass
#> solution
values = sorted(map(int, input().split()))
#< solution
#> validate input
assert 3 <= len(values) <= 5000
assert len(values) == len(set(values))
assert all(-10_000_000_000 <= x <= 10_000_000_000 for x in values)
#< validate input
#> solution
S = set(values)
for i, x in enumerate(values):
    for y in values[i+1:]:
        z = -(x + y)
        if z <= y:
            break
        if z in S:
            assert x < y < z and x + y + z == 0
            print(x, y, z)
#< solution