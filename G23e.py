'''
    KNOWN

    Assume we are given a list of pairs of names, where each pair denotes
    that the first person knows the second person. If a person is known by
    all other persons mentioned, we say that the person is "known". 
    Your task is to list all known persons in alphabetic order.

    The below list of pairs contains four names: Guido, Bjarne, Niklaus, and 
    Kristen. Guido is the only one that is known by the three others.

        Guido Bjarne
        Niklaus Guido
        Kristen Guido
        Bjarne Guido
        Niklaus Kristen

    Input:  The first line contains an integer k, the number of pairs where
            1 <= k <= 100. The following k lines contain two names a and b,
            separated by a space, denoting that a knows b. It is guaranteed 
            that all pairs are distinct and a != b for all pairs.

    Output: The list of all known persons in alphabetic order, separated by 
            spaces. If there are no known person output "-".

    Example:

      Input:  5
              Guido Bjarne
              Niklaus Guido
              Kristen Guido
              Bjarne Guido
              Niklaus Kristen
            
      Output: Guido             
'''


# insert code
pass
#> solution
k = int(input())
#< solution
#> validate input
assert 1 <= k <= 100
#< validate input
#> solution
knows = dict()
for _ in range(k):
    a, b = input().split()
    for x in (a, b):
        if x not in knows:
            knows[x] = set()
#< solution
#> validate input
    assert a != b
    assert a not in knows[b]
#< validate input
#> solution
    knows[b].add(a)
known = [name for name, others in knows.items() if len(others) == len(knows) - 1]
if not known:
    print('-')
else:
    print(*sorted(known))
#< solution
