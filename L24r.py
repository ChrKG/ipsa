'''
    FROGGY

    You are jumping around on an integer grid. At each time step you can jump to 
    a grid cell within distance d of your current position, where the distance 
    between two grid cells is the Euclidean distance between the cell centers. 
    You can freely choose your start position. At each step exactly one grid 
    cell is green. If you are on the green cell, you get a point. 
    What is the maximum number of points you can get, if you know the positions 
    of all green cells in advance?

    Input:  The first line contains two integers n and d, where 1 <= n <= 25 is
            the number of time steps, and 1 <= d <= 25 is the jump radius.
            Each of the following n lines contains two integers x and y, 
            where 0 <= x <= 25 and 0 <= y <= 25, where the i'th line is 
            the position of the green cell at time step i.

    Output: A single integer, the maximum number of points you can get.

    Example: 
    
      Input:  3 5
              5 0
              0 5
              5 10

      Output: 2

      In this example we have n = 3 points and jump radius d = 5.
      You can start at (5, 0) [that is green and score a point],
      jump to (5, 5) [not scoring a point, since (0, 5) is now green], and then
      jump to (5, 10) [scoring a point, since this cell is now green]. 
      In total you score 2 points, and this is the best possible.
'''


# insert code
pass
#> solution
from functools import cache

n, d = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
#< solution
#> validate input
assert 1 <= n <= 25
assert 1 <= d <= 25
assert all(0 <= x <= 25 and 0 <= y <= 25 for x, y in points)
#< validate input
#> solution
xs, ys = zip(*points)
cells = [(x, y) for x in range(min(xs), max(xs)+1) for y in range(min(ys), max(ys)+1)]

@cache
def score(step, cell):
    best = 0
    if step < n: 
        x, y = cell
        for cell_ in cells:
            x_, y_ = cell_
            if (x_ - x)**2 + (y_ - y)**2 <= d**2:
                best = max(best, score(step+1, cell_))
        if points[step] == cell:
            best += 1   
    return best

print(max(score(0, start) for start in cells))
#< solution
