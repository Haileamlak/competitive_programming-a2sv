class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) // k < m:
            return -1

        def bouqout_on_day(day):
            res = 0
            count = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    count += 1
                else:
                    count = 0
                
                if count == k:
                    res += 1
                    count = 0
            
            return res
        
        min_day = 1
        max_day = pow(10, 9)
        while min_day <= max_day:
            mid = min_day + (max_day - min_day) // 2
            if bouqout_on_day(mid) >= m:
                max_day = mid - 1
            else:
                min_day = mid + 1
        
        return min_day