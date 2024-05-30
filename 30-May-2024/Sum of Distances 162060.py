# Problem: Sum of Distances - https://leetcode.com/problems/sum-of-distances/

class Solution(object):
    def distance(self, nums):
        indexes = {}

        for i in range(len(nums)):
            if nums[i] in indexes:
                indexes[nums[i]].append(i)
            else:
                indexes[nums[i]] = [i]
        
        for num, idxs in indexes.items():
            
            total = sum(idxs)
            curr = 0
            p = 0
            s = len(idxs)
            for i in idxs:
                curr += i
                total -= i
                p += 1
                s -= 1
                nums[i] = ((p * i) - curr) + ((total) - (i * (s)))

        return nums
        