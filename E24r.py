'''
    POPULAR

    Your are given k groups, where each group contains a list of items, 
    possibly with repetitions. You have to list the items that appear in at
    least half of the groups in sorted order.

    In the below three groups, only COKE and WATER appears in at least half of
    the groups.
    
        Group 1      Group 2       Group 3
        ----------------------------------
        TEA          WATER         COKE
        COFFEE       COKE          WATER
        SPRITE       JUICE         COCOA
        PEPSI
        COKE
        PEPSI
        PEPSI

    Input:  The first line contains an integer k, 1 <= k <= 25, the number of
            groups. The next lines contains the content of the k groups. The 
            first line for each group is the number n of items in the group, 
            where 1 <= n <= 100, followed by n lines, the items in the group,
            one item per line. Each item is a string with capital letters only.

    Output: The items that appear in at least half of the groups in sorted order,
            one item per line. If no item appears in at least half of the groups, 
            print "NOTHING POPULAR".

    Example:

      Input:  3
              7
              TEA
              COFFEE
              SPRITE
              PEPSI
              COKE
              PEPSI
              PEPSI
              3
              WATER
              COKE
              JUICE
              3
              COKE
              WATER
              COCOA

      Output: COKE
              WATER
'''


# insert code
pass
#> solution
from collections import Counter

k = int(input())
#< solution
#> validate input
assert 1 <= k <= 25
#< validate input
#> solution
fq = Counter()
for _ in range(k):
    n = int(input())
    values = [input() for _ in range(n)]
#< solution
#> validate input
    assert 1 <= n <= 100
    assert all('A' <= c <= 'Z' for value in values for c in value)
#< validate input
#> solution
    fq += Counter(set(values))
popular = sorted(key for key, value in fq.items() if 2 * value >= k)
if popular:
    for key in popular:
        print(key)
else:
    print('NOTHING POPULAR')
#< solution
