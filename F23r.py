'''
    STRING FORMAT

    Your task is to write a function string_format(text), that takes a string
    and returns a new string containing the input string formatted according
    to the following optional keyword arguments to string_format:

      spacing=value
      
        Add spacing copies of the fill character '.' between each character 
        in the input string. Default is spacing=0. Example:

            string_format('STRING', spacing=3) == 'S...T...R...I...N...G'

      fill=symbol

        Instead of using '.' as the fill character use symbol. Example:

            string_format('STRING', spacing=2, fill='_') == 'S__T__R__I__N__G'

      width=value

        The resulting string should be of length value. It is required that 
        value is greater than or equal to the length of the input string 
        after applying the spacing argument. The string will be padded with the
        fill character left and right according to the alignment argument below.

      alignment=value

        value should either be the string 'left', 'right' or 'center'.
        Default is 'left'. If 'left', the input string is padded on the right.
        If 'right', the input string is padded on the left. If 'center', the
        input string is padded on both sides such that the left side is at most
        one character longer than the right side. Examples:

        string_format('STRING', spacing=1, width=25, alignment='left')
            == 'S.T.R.I.N.G..............'
    
        string_format('STRING', spacing=1, width=25, alignment='right')
            == '..............S.T.R.I.N.G'

        string_format('STRING', spacing=1, width=25, alignment='center')
            == '.......S.T.R.I.N.G.......'

    Input:  A python expression using the function string_format. 

    Output: The result of evaluating the expression.

    Example:

      Input:  string_format('Python', width=31, alignment='center', spacing=2)

      Output: ........P..y..t..h..o..n.......

    Note: The below code already reads the input and prints the output of
          evaluating the expression.
'''


# insert code
def string_format(text):
    pass
#> solution
def string_format(text, width=None, alignment='left', spacing=0, fill='.'):
#< solution
#> validate input
    assert isinstance(text, str)
    assert width is None or isinstance(width, int)
    assert alignment in ('left', 'right', 'center')
    assert isinstance(spacing, int) and spacing >= 0
    assert isinstance(fill, str) and len(fill) == 1 and fill != ' '
#< validate input
#> solution
    if width is None:
        width = len(text) + (len(text) - 1) * spacing
#< solution
#> validate input
    assert width >= len(text) + (len(text) - 1) * spacing
#< validate input
#> solution
    text = (fill * spacing).join(text)
    if alignment == 'left':
        return text.ljust(width, fill)
    if alignment == 'right':
        return text.rjust(width, fill)
    if (width - len(text)) % 2 == 0:
        return text.center(width, fill)
    else:
        return fill + text.center(width - 1, fill)
#< solution


print(eval(input()))
