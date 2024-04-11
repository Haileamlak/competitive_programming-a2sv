# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination = []
        candidates.sort()

        def back_track(index, curr_sum):
            if curr_sum == target:
                combinations.append(combination.copy())
                return
            
            if index == len(candidates):
                return

            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1

            combination.append(candidates[index])
            if curr_sum + candidates[index] <= target:
                back_track(index + 1, curr_sum + candidates[index])
            combination.pop()
            if curr_sum <= target:
                back_track(next_index, curr_sum)

        back_track(0, 0)
        return combinations