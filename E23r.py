'''
    MISSING

    You are given two lists of names. The second list contains a subset of the
    names in the first list. Your task is to print the missing names from the
    first list in sorted order.

    Input:  The first line contains a positive integer n, the number of names 
            in the first list. Then follows n lines, each containing a name.
            Then follows a positive integer m, the number of names in the
            second list, followed by m lines, each containing a name.
            All names in each of the lists are distinct, and all names only
            contain letters. The second list is a subset of the first list.
            1 <= m <= n <= 100.

    Output: Sorted list of the names only in the first list, one name per line.

    Example:

      Input:  5
              Goofy
              Micky
              Scrooge
              Donald
              Daisy
              3
              Micky
              Daisy
              Goofy

      Output: Donald
              Scrooge
'''


# insert code
pass
#> solution
n = int(input())
names = [input() for _ in range(n)]
m = int(input())
exclude = [input() for _ in range(m)]
#< solution
#> validate input
assert 1 <= n <= 100
assert 0 <= m <= n
assert all(name.isalpha() for name in names)
assert len(names) == len(set(names))
assert all(name.isalpha() for name in exclude)
assert len(exclude) == len(set(exclude))
assert set(exclude) <= set(names)
#< validate input
#> solution
print(*sorted(set(names) - set(exclude)), sep='\n')
#< solution
