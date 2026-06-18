'''
    REPLACE

    Write a function replace(text, substitutes) that takes a string text 
    consisting of space separated words and a dictionary substitutes,
    that consists of key-value pairs where both the key and the value are
    single words, returns a new string where each word in the text, that is a 
    key in substitutes, is replaced by the associated word in the dictionary.
    
    E.g., if 
    
       text = 'COPENHAGEN IS GREAT' and 
       substitutes = {'COPENHAGEN': 'AARHUS', 'GREAT': 'FANTASTIC'}, 

    then the function replace should return 'AARHUS IS FANTASTIC'.

    Input:  Two lines. The first line contains a text consisting of space
            separated words. The second line contains a Python dictionary 
            substitutes containing the possible string replacements.
            All words in the text, and keys and values in the dictionary 
            are single words containing upper case letters only.

    Output: The result of calling replace(text, substitutes).

    Example:

      Input:  COPENHAGEN IS GREAT
              {'COPENHAGEN': 'AARHUS', 'GREAT': 'FANTASTIC'}

      Output: AARHUS IS FANTASTIC

    Note: The below code already reads the input and calls replace.
'''


def replace(text, substitutes):
    # insert code
    pass
#> solution
    return ' '.join(substitutes.get(word, word) for word in text.split())
#< solution


text = input()
replacements = eval(input())
#> validate input
assert len(text) <= 1000
assert text == text.strip()
words = text.split(' ')
assert all(word.isalpha() and word.isupper() for word in words)
assert all(k.isalpha() and v.isalpha() and k.isupper() and v.isupper() for k, v in replacements.items())
#< validate input
print(replace(text, replacements))
