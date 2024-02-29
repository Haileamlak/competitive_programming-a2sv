class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        subset = []

        picked = set()
        
        def back_track(index):
            if index == len(nums):
                subsets.add(tuple(sorted(subset)))
            
            for i in range(index, len(nums)):
                if nums[i] not in picked:
                    subset.append(nums[i])
                    # picked.add(nums[i])
                    
                    back_track(i + 1)

                    subset.pop()
                    # picked.remove(nums[i])
                # picked.add(nums[i])
                back_track(i + 1)
                # picked.add(nums[i])

        back_track(0)
        return list(subsets)