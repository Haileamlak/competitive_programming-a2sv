class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []
        combination = []

        def back_track(num, curr_sum):
            if curr_sum == n and len(combination) == k:
                combinations.append(combination.copy())
                return
            
            if num == 10 or len(combination) >= k:
                return
            
            if curr_sum + num <= n:
                combination.append(num)
                back_track(num + 1, curr_sum + num)
                combination.pop()
            
            if curr_sum <= n:
                back_track(num + 1, curr_sum)
        
        back_track(1, 0)
        return combinations