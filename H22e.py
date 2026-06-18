'''
    DRAW

    In this exercise you are going to make simple ASCII drawings, consisting
    of a rectangle containing '.' and 'X'. Initially all characters are '.'.
    The lower left position is (0, 0), and the upper right position is
    (width - 1, height - 1). A line from position (x0, y0) to position (x1, y1)
    is drawn with 'X', including both end positions. If both end positions are
    equal, the line only consists of a single 'X'.

    The first example below shows a rectangle with width=6 and height=4,
    and a single line from lower-left (2, 1) to upper-right (4, 3).

    It is guaranteed that each line is vertical, horizontal or has a slope
    of 45 degrees, i.e. abs(x1 - x0) == abs(y1 - y0).

    Input:  The first line contains three space separated integers width,
            height and n. The following n lines each contains four space
            separated integers x0, y0, x1 and y1, each defining a line
            from (x0, y0) to (x1, y1), both end positions inclusive.

            It is guaranteed that 1 <= width <= 25 and 1 <= height <= 25,
            and n <= 25.

    Output: Height lines, each line with width characters, either '.' or 'X',
            as defined by the n lines in the input.

    Example:

      Input:  6 4 1
              2 1 4 3

      Output: ....X.
              ...X..
              ..X...
              ......

      Input:  19 16 13
              2 1 16 1
              2 7 16 7
              2 2 2 6
              16 2 16 6
              5 2 5 5
              7 2 7 5
              10 3 10 5
              13 3 13 5
              11 3 12 3
              11 5 12 5
              6 5 6 5
              3 8 9 14
              15 8 10 13

      Output: ...................
              .........X.........
              ........X.X........
              .......X...X.......
              ......X.....X......
              .....X.......X.....
              ....X.........X....
              ...X...........X...
              ..XXXXXXXXXXXXXXX..
              ..X.............X..
              ..X..XXX..XXXX..X..
              ..X..X.X..X..X..X..
              ..X..X.X..XXXX..X..
              ..X..X.X........X..
              ..XXXXXXXXXXXXXXX..
              ...................
'''


# insert code
pass
#> solution
width, height, n = map(int, input().split())
assert 1 <= width <= 25 and 1 <= height <= 25 and n <= 25
canvas = [['.'] * width for _ in range(height)]
for _ in range(n):
    x0, y0, x1, y1 = map(int, input().split())
    
    assert 0 <= x0 < width
    assert 0 <= x1 < width
    assert 0 <= y0 < height
    assert 0 <= y1 < height
    assert x0 == x1 or y0 == y1 or abs(x1 - x0) == abs(y1 - y0)
    
    d = max(abs(x1 - x0), abs(y1 - y0), 1)

    for i in range(d + 1):
        canvas[y0 + i * (y1 - y0) // d][x0 + i * (x1 - x0) // d] = 'X'

for row in reversed(canvas):
    print(*row, sep='')
#< solution
