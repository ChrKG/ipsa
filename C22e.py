'''
    BLOCK

    Write a program that prints a rectangular block with the same symbol.
    The program should read three lines: the first line the number of
    rows to output, the second line the number of columns to output,
    and the last line the symbol to repeat rows * columns times.
 
    Input:  1st line the integer rows (1 <= rows <= 25).
            2nd line the integer columns (1 <= columns <= 25).
            3rd line the single printable character symbol (not whitespace).

    Output: rows lines each with columns copies of symbol.

    Example:

      Input:  3
              5
              x

      Output: xxxxx
              xxxxx
              xxxxx
'''


# insert code
pass

#> solution
rows = int(input())
columns = int(input())
symbol = input()
assert 1 <= rows <= 25
assert 1 <= columns <= 25
assert len(symbol) == 1
for _ in range(rows):
    print(symbol * columns)
#< solution
