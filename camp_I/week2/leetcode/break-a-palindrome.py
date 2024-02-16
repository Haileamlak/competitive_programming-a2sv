class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        
        index = 0
        while index < len(palindrome) and palindrome[index] == 'a': 
            index += 1
        
        if (len(palindrome) % 2 != 0 and index == len(palindrome) // 2):
            index += 1
            while index < len(palindrome) and palindrome[index] == 'a': 
                index += 1

        non_palindrome = list(palindrome)

        if index == len(palindrome):
            non_palindrome[-1] = 'b'
        else:
            # if :
            non_palindrome[index] = 'a'

        return ''.join(non_palindrome)