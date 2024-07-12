# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        res = 0
        count = 1
        j = 0
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                chars[j] = chars[i - 1]
                j += 1
                if count == 1:
                    res += 1
                else:
                    res += 1 + ceil(log(count + 1, 10))
                    for ch in str(count):
                        chars[j] = ch
                        j += 1
                
                count = 1
        
        
        chars[j] = chars[-1]
        j += 1
        if count == 1:
            res += 1
        else:
            res += 1 + ceil(log(count + 1, 10))
            for ch in str(count):
                chars[j] = ch
                j += 1

        return res