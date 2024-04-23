# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {letter: letter for letter in ascii_lowercase}

        def find(letter):
            while letter != parent[letter]:
                parent[letter] = parent[parent[letter]]
                letter = parent[letter]
            
            return letter
        
        def union(letter1, letter2):
            parent1 = find(letter1)
            parent2 = find(letter2)

            if parent1 < parent2:
                parent[parent2] = parent1
            else:
                parent[parent1] = parent2
        
        for letter1, letter2 in zip(s1, s2):
            union(letter1, letter2)
        
        res = []
        for letter in baseStr:
            res.append(find(letter))
        
        return ''.join(res)