'''
    SQUARE SUM

    Write a function square_sum(a, b) that takes two integers a and b, a <= b, 
    and returns the sum of all squares x**2, where x is a positive integer 
    and a <= x**2 <= b.

    E.g., square_sum(100, 200) = 730, since 
    
        10 ** 2 = 100 
        11 ** 2 = 121 
        12 ** 2 = 144
        13 ** 2 = 169
        14 ** 2 = 196

        100 + 121 + 144 + 169 + 196 = 730.

    Input:  A single line containing two integers a and b, 
            where 1 <= a <= b <= 1_000_000_000.

    Output: The sum of all squares x**2, where x is an integer and a <= x**2 <= b.

    Example:

      Input:  100 200   

      Output: 730

    Note: The below code already reads a and b, and calls square_sum(a, b).
'''


def square_sum(a, b):
    # insert code
    pass
#> solution
    # Slow solution
    #return sum([x for x in range(a, b + 1) if (x ** 0.5).is_integer()])
    # Fast solution
    import math
    return sum(x**2 for x in range(math.ceil(a ** 0.5), math.floor(b ** 0.5) + 1))
#< solution


a, b = map(int, input().split())
#> validate input
assert 1 <= a <= b <= 1_000_000_000
#< validate input
print(square_sum(a, b))
