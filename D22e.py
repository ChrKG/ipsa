'''
    PLUSMINUS

    Write a function plusminus(x1, x2, x3, ..., xk) that can take zero
    or more integer arguments and returns x1 - x2 + x3 - x4 + x5 - ...
    E.g. plusminus(10, 5, 6, 2) = 10 - 5 + 6 - 2 = 9.

    Input:  A Python expression using the function plusminus.

    Output: The result of evaluating the expression.

    Example:

      Input:  plusminus(10, 5, 6, 2)

      Output: 9

    Note: The below code already handles reading the input.
'''


# insert code
def plusminus():
    pass
#> solution
def plusminus(*x):
    assert all(isinstance(xi, int) for xi in x)
    return sum(x[::2]) - sum(x[1::2])
#< solution


print(eval(input()))
