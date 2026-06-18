'''
    CAPITALS

    Remove all lower case letters from a string.

    Input:  A single line with a string containtin lower and capital letters,
            and length between 1 and 100.

    Output: The input string with all lower case letters removed.

    Example:

      Input:  ComeLateAndStartSleeping

      Output: CLASS
'''


# insert code
pass
#> solution
s = input()
assert 1 <= len(s) <= 100
assert all('a' <= c <= 'z' or 'A' <= c <= 'Z' for c in s)
print(''.join(c for c in s if 'A' <= c <= 'Z'))
#< solution
