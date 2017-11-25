# Look-and-say sequences

from itertools import groupby
from re import findall

n = 50

# Use regex matching.
seq = '1113122113'
for i in range(n):
    groups = findall(r'(\d)(\1*)', seq)
    new_seq = ''
    for g in groups:
        # groups contains tuples of two elements (one for each set of capturing
        # parentheses), so combine the lengths of g[0] and g[1].
        new_seq += str(len(g[0]) + len(g[1])) + g[0]
    seq = new_seq

print(len(seq))

# Use groupby from itertools.
seq = '1113122113'
for i in range(n):
    new_seq = ''
    for k,g in groupby(seq):
        new_seq += str(len(list(g))) + k
    seq = new_seq

print(len(seq))
