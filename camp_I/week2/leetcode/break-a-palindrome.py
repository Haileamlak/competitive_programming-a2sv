class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        
        index = 0
        while index < len(palindrome) // 2 and palindrome[index] == 'a': 
            index += 1
        
        non_palindrome = list(palindrome)

        if index >= len(palindrome) // 2:
            non_palindrome[-1] = 'b'
        else:
            non_palindrome[index] = 'a'

        return ''.join(non_palindrome)