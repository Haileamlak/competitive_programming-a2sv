class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        curr = 0
        for ch in s:
            if ch == '|':
                curr += 1
            
            candles.append(curr)

        res = []
        for query in queries:
            left = query[0]
            if (query[0] > 0 and candles[query[0]] == candles[query[0] - 1]) or candles[query[0]] == 0:
                left = bisect_right(candles, candles[query[0]])

            right = bisect_left(candles, candles[query[1]])
            if right <= left:
                res.append(0)
            else:
                res.append(right - left - candles[right] + candles[left])
        
        return res