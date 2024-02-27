def permut(s):
    perm = set(itertools.permutations(s))
    for i in perm:
        print(*i, sep='')
import itertools 

permut(input())