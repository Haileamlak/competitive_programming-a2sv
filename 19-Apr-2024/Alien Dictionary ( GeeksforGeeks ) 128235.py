# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

from collections import defaultdict, deque

class Solution:
    def findOrder(self,alien_dict, N, K):
        graph = {}
        letters = set()
        for word in alien_dict:
            letters = letters.union(set(word))
        
        for letter in letters:
            graph[letter] = []
            
        indegree = defaultdict(int)
        
        def add_edge(word1, word2):
            for letter1, letter2 in zip(word1, word2):
                if letter1 != letter2:
                    graph[letter1].append(letter2)
                    indegree[letter2] += 1
                    break
        
        for i in range(N - 1):
            add_edge(alien_dict[i], alien_dict[i + 1])
    
        queue = deque()
        for letter in graph:
            if letter not in indegree:
                queue.append(letter)
        
        res = []
        while queue:
            curr_letter = queue.popleft()
            res.append(curr_letter)
            
            for next_letter in graph[curr_letter]:
                indegree[next_letter] -= 1
                
                if indegree[next_letter] == 0:
                    queue.append(next_letter)
        
        return res