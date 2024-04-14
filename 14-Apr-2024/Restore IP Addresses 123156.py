# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        stack = []

        def backtrack(index):
            if index == len(s):
                if len(stack) == 4:
                    result.append('.'.join(stack))
                    
                return
            
            if len(stack) == 4:
                return 
            
            if s[index] == '0':
                stack.append('0')
                backtrack(index + 1)
                stack.pop()
                return 

            for i in range(index + 1, len(s) + 1):
                curr = s[index:i]
                if int(curr) > 255:
                    break

                stack.append(curr)
                backtrack(i)
                stack.pop()
                
        backtrack(0)

        return result