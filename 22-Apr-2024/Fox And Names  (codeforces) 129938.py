# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque
from string import ascii_lowercase

words = []

n = int(input())
for _ in range(n):
    words.append(input())

graph = defaultdict(list)
indegree = defaultdict(int)

def add_edge(word1, word2):
    for letter1, letter2 in zip(word1, word2):
        if letter1 != letter2:
            graph[letter1].append(letter2)
            indegree[letter2] += 1
            
            return True
    else:
        if len(word1) > len(word2):
            return False

        return True

for i in range(n - 1):
    if not add_edge(words[i], words[i + 1]):
        print('Impossible')
        exit()

queue = deque([letter for letter in ascii_lowercase if letter not in indegree])

res = []
while queue:
    curr_letter = queue.popleft()
    res.append(curr_letter)

    for next_letter in graph[curr_letter]:
        indegree[next_letter] -= 1

        if indegree[next_letter] == 0:
            queue.append(next_letter)
    
if len(res) == 26:
    print(''.join(res))
else:
    print('Impossible')