# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = list(map(int, version1.split('.')))
        b = list(map(int, version2.split('.')))

        a.extend(max(0, len(b) - len(a)) * [0])
        b.extend(max(0, len(a) - len(b)) * [0])

        for revision1, revision2 in zip(a, b):
            if revision1 < revision2:
                return -1
            elif revision1 > revision2:
                return 1
        
        return 0