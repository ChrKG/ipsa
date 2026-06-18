'''
    DOUBLE WORDS

    Given a string find all words that appear twice in a row in the string.

    E.g., in the below string the words 'TREES' and 'BIRDS' appear twice in a row.

      THE FOREST CONTAINS TREES TREES TREES AND MORE TREES AND BIRDS BIRDS AND BIRDS

    Input:  A singe line containing a string of words separated by spaces. 
            Each word contains uppercase letters only.

    Output: A single line with the words that appear twice in a row in the 
            string, with no word repeated in the output, and the words appearing
            sorted in alphabetical order. If no word appears twice in a row,
            output '-'.

    Example:

      Input:  THE FOREST CONTAINS TREES TREES TREES AND MORE TREES AND BIRDS BIRDS AND BIRDS

      Output: BIRDS TREE
'''


# insert code
pass
#> solution
words = input().split()
#< solution
#> validate input
assert 1 <= len(words) <= 100
assert all('A' <= c <= 'Z' for w in words for c in w) 
#< validate input
#> solution
doubles = set(w for i, w in enumerate(words[:-1]) if w == words[i + 1])
if doubles:
    print(*sorted(doubles))
else:
    print('-')
#< solution
