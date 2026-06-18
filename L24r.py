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
