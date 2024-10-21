# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution(object):
    def isLongPressedName(self, name, typed):
        i = j = 0
        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                return False

            i += 1
            j += 1

            top = 0
            while i < len(name) and name[i] == name[i - 1]: 
                i += 1
                top += 1

            bottom = 0
            while j < len(typed) and typed[j] == typed[j - 1]:
                j += 1
                bottom += 1
            
            if bottom < top:
                return False

        if i < len(name) or j < len(typed):
            return False
            
        return True