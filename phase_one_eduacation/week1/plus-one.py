class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(list(map(str, digits))))
        number += 1
        
        return list(map(int, list(str(number))))