# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = {_str: _str for _str in strs}
        size = {_str: 1 for _str in strs}

        def get(x):
            root = x
            while root != parent[root]:
                root = parent[root]
            
            while x != parent[x]:
                x, parent[x] = parent[x], root
            
            return x
        
        def union(x, y):
            px, py = get(x), get(y)

            if px != py:
                if size[px] > size[py]:
                    px, py = py, px
                
                parent[px] = py
                size[py] += size[py]
        
        def are_similar(str1, str2):
            difference = 0
            for letter1, letter2 in zip(str1, str2):
                difference += (letter1 != letter2)
            
            return difference <= 2
        
        for i in range(len(strs)):
            for j in range(len(strs)):
                word1, word2 = strs[i], strs[j]
                if are_similar(word1, word2):
                    union(word1, word2)
        
        res = 0
        for i, par in parent.items():
            res += (i == par)
        
        return res