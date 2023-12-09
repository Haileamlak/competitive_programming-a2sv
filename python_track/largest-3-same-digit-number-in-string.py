class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        for i in range(3, len(num) + 1):
            temp_good = num[i - 3:i]
            if temp_good.count(temp_good[0]) == 3:
                if len(max_good) == 0:
                    max_good = temp_good 
                elif temp_good[0] > max_good[0]: 
                    max_good = temp_good
                    
        return max_good