'''
    KNIGHT

    Given an n x n chessboard with a single knight at position (i, j), 
    determine the possible positions of the knight after d moves.

    A knight's movement is: it moves two squares vertically and one square
    horizontally, or two squares horizontally and one square vertically 
    If 'K' marks the position of the knight before the move, then 'X' are the
    possible positions after one move.
    
        ........
        ..X.X...
        .X...X..
        ...K....
        .X...X..
        ..X.X...
        ........
        ........

    and after two moves:

        X.X.X.X.
        ...X...X
        X.X.X.X.
        .X.X.X.X
        X.X.X.X.
        ...X...X
        X.X.X.X.
        .X.X.X..

    Input:  A single line with four integers n, i, j and d, separated by spaces,
            where n is the size of the board, (i, j) is the position of the
            knight, and d is the number of moves. We assume i is the row number,
            j is the column number, and the top-left cell is (0, 0).
            It is guaranteed that 5 <= n <= 100, 0 <= i < n, 0 <= j < n, 
            and 0 <= d <= 100.

    Output: The n x n board after d moves, where the possible knight positions 
            are marked by 'X', and all other cells are marked by '.'.
            Only mark positions where the knight can be after _exactly_ d moves.

    Example:

      Input:  8 3 3 2

      Output: X.X.X.X.
              ...X...X
              X.X.X.X.
              .X.X.X.X
              X.X.X.X.
              ...X...X
              X.X.X.X.
              .X.X.X..
'''


# insert code
pass
