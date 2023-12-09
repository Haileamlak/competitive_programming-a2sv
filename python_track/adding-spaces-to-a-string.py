class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        modified = ''
        last = 0
        for index in spaces:
            modified += s[last:index] + ' '
            last = index
        
        modified += s[last:]

        return modified