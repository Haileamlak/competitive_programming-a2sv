class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination = []

        candidates.sort()

        def back_track(index, curr_sum):
            if curr_sum == target:
                combinations.append(combination.copy())
                return
            
            if index == len(candidates): 
                return 
            
            if curr_sum + candidates[index] <= target:
                combination.append(candidates[index])
                back_track(index, curr_sum + candidates[index])
                combination.pop()

            if curr_sum <= target:
                back_track(index + 1, curr_sum)
        
        back_track(0, 0)

        return combinations