'''
    REPEATING WORDS

    Input:

       A single line with at most 100 characters containing words separated by 
       a single space, each word consisting of lower case letters 'a'-'z'. 
       The input contains at least one word.

    Output:

       A single line with the same words, but where words repeated multiple times
       after each other are replaced by a single occurrence of the word.

    Example:

       Input:  this this line contains the the the same word word repeated multiple multiple times times times

       Output: this line contains the same word repeated multiple times
'''


# insert code

pass

#> solution
line = input()
assert line == line.strip()
assert len(line) <= 100
assert all(c == ' ' or 'a' <= c <= 'z' for c in line)
assert '  ' not in line
words = line.split()
print(words[0], *[word for previous, word in zip(words, words[1:]) if previous != word])
#< solution
