class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [ch for ch in s]
        s = list(filter(lambda x:x.isalnum(), s))

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        
        return True