class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        
        index = 0
        while index < len(palindrome): 
            if palindrome[index] != 'a' and ((len(palindrome) % 2 == 0 or index != len(palindrome) // 2)):
                break

            index += 1
        
        non_palindrome = list(palindrome)

        if index == len(palindrome):
            non_palindrome[-1] = 'b'
        else:
            non_palindrome[index] = 'a'

        return ''.join(non_palindrome)