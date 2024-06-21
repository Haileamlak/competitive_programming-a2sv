# Problem: D - Rizzler's String - https://codeforces.com/gym/527294/problem/D

import sys
input = lambda: sys.stdin.readline().rstrip()

mod = 10**9 + 7
s = input()

sequences = 0
before_last_b = 0 # the number of valid sequences before the last b

for idx, char in enumerate(s):
    if char == 'b':
        # all 'a's that come after now can immediately follow this 'b'
        # hence we can use all the valid sequences we have so far as prefixes of the next sequences we form
        before_last_b = sequences
    
    elif char == 'a':
        # this 'a' can be appended to sequences we formed before the last 'b' -> before_last_b
        # this character can also be a start of a new sequence, so we add 1
        sequences += before_last_b + 1
        sequences %= mod

print(sequences)