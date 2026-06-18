'''
    STARS

    Your task is to create a function 'print_stars', that given a list
    of (name, score) prints each name followed by score copies of '*'. 
    All names should be appended by underscores '_', so that all names
    become equal length. A single additional '_' should be printed 
    between names and stars.

    Example:
    
        stars = [('JOHN', 2), ('JOE', 3), ('ALEXANDER', 2), ('VICTOR', 0), ('ALBERT', 5)]
        print_stars(stars)

    example output:

        JOHN______**
        JOE_______***
        ALEXANDER_**
        VICTOR____
        ALBERT____*****

    The function print_stars should take two optional keyword arguments
    'alphabetically' and 'highscore', such that

        print_stars(stars, alphabetically=True)

    prints the names in alphabetically order, whereas 

        print_stars(stars, highscore=True)

    prints the names sorted in decreasing score order, where names with
    equal score should be printed alphabetically (see test files for
    examples). If neither alphabetically or highscore are True, names
    should be printed in the order given in the input.

    Finally, print_stars should accept an optional argument 'vertical',
    that prints the scores vertically (and can be combined with arguments
    highscore and alphabetically). See example below. Each name is printed
    top-down with stars above, and underscores below and above to make
    all columns have equal length and names starting in same row.
    All rows should have equal length, and score columns separated by
    underscores.

    Example:

        print_stars(start, vertical=True, highscore=True)

    example output:
    
        *________
        *________
        *_*______
        *_*_*_*__
        *_*_*_*__
        A_J_A_J_V
        L_O_L_O_I
        B_E_E_H_C
        E___X_N_T
        R___A___O
        T___N___R
        ____D____
        ____E____
        ____R____

    Input:  A single Python expression calling print_stars.
            At most one of the keyword arguments alphabetically
            and highscore will be True.
            There are 1..20 distinct names.
            Each name as length 1-20 and contains only characters A-Z.
            Scores are integers 0..5.

    Output: The result of calling print_stars.

    Note: The below code already reads the input and calls print_stars.
'''


def print_stars(stars):
    # insert code

    pass  

#> solution
def print_stars(stars, *, alphabetically=False, highscore=False, vertical=False):
    names, scores = zip(*stars)
    max_name = max(map(len, names))
    max_score = max(scores)

    assert not alphabetically or not highscore
    assert len(names) == len(set(names))
    assert all('A' <= c <=  'Z' for name in names for c in name)
    assert all(1 <= len(name) <= 20 for name in names)
    assert 1 <= len(stars) <= 100

    if alphabetically:
        stars.sort()
    if highscore: 
        stars.sort(key=lambda score: (-score[1], score[0]))
    if not vertical:
        for name, score in stars:
            print(name + '_' * (max_name - len(name) + 1) + '*' * score)
    else:
        for i in range(max_score, 0, -1):
            print('_'.join('*' if score >= i else '_' for name, score in stars))
        for i in range(max_name):
            print('_'.join(name[i] if i < len(name) else '_' for name, score in stars))
#< solution

eval(input())
