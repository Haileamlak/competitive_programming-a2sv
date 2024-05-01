# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0':
            return '0'
            
        res = []

        a, b = int(a, 2), int(b, 2)
        carry = 0

        while a or b:
            curr = (a & 1) + (b & 1) + carry
            res.append(str(curr % 2))
            carry = curr // 2
            a >>= 1
            b >>= 1
        
        return (str(carry) + ''.join(reversed(res))).lstrip('0')