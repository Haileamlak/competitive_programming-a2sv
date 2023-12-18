class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_arr = [ch for ch in s]
        i = 0
        while i < len(s):
            j = 0
            end = min(k - 1, len(s) - i - 1)
            while j < end:
                s_arr[i + j], s_arr[i + end] = s_arr[i + end], s_arr[i + j]

                j += 1
                end -= 1
            
            i += 2*k
        
        return ''.join(s_arr)