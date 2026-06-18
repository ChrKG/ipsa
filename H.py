'''
    UNIQUE VALUES

    Your task is to write a function uniques(D), that takes a
    dictionary D, and returns a list or all the keys in the dictionary,
    where the associated value does not occur as the value for another
    key. The returned list should be in sorted order.

    Input:

        A single line with a Python dictionary D, where we assume that
        both keys and values are immutable.

    Output:

        A single line with a sorted Python list of the keys in D with
        an associated unique value.

    Example:

      Input:  {'B': 3, 'D': 1, 'A': 2, 'F': 7, 'E': 3, 'G': 4}

      Output: ['A', 'D', 'F', 'G']

    Note: 

      Your task is only to implement the function uniques.  The
      provided code already takes care of the needed input-output.
'''


def uniques(D):
    pass  # add your code here


dictionary = eval(input())
print(uniques(dictionary))
