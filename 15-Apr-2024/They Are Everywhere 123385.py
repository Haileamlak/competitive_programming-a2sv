# Problem: They Are Everywhere - https://codeforces.com/problemset/problem/701/C

from collections import defaultdict


n = int(input())
word = input()

unique = set(word)
window = defaultdict(int)

res = n
left = 0
for right in range(n):
    window[word[right]] += 1
    
    while len(window) >= len(unique):
        window[word[left]] -= 1

        if window[word[left]] == 0:
            del window[word[left]]
        
        left += 1
    
    if left > 0:
        res = min(res, right - left + 2)

print(res)