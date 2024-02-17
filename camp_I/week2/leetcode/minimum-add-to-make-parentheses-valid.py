class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening_brackets = 0
        closing_brackets = 0

        for bracket in s:
            if bracket == '(':
                opening_brackets += 1
            elif opening_brackets:
                opening_brackets -= 1
            else:
                closing_brackets += 1
        
        return opening_brackets + closing_brackets