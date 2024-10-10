# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        result = []
        for word in words:
            if word[0].lower() in row1:
                row = row1
            
            elif word[0].lower() in row2:
                row = row2
            
            else:
                row = row3

            for letter in word:
                if letter.lower() not in row:
                    break
            else:
                result.append(word)

        return result