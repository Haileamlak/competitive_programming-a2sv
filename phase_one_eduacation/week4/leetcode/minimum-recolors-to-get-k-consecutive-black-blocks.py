class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = k
        window = Counter(blocks[:k - 1])
        for i in range(k - 1, len(blocks)):
            window[blocks[i]] += 1
            res = min(res, window['W'])
            
            window[blocks[i - k + 1]] -= 1
        
        return res
