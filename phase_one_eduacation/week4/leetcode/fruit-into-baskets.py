class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        unique = 0
        window = defaultdict(int)

        left = 0
        for right in range(len(fruits)):
            if fruits[right] not in window:
                unique += 1
            window[fruits[right]] += 1

            while unique > 2:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                    unique -= 1
                    
                left += 1
            
            res = max(res, right - left + 1)
        
        return res