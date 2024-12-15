# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = [num1 - num2 for num1, num2 in zip(nums1, nums2)]

        res = 0
        def merge(left_arr, right_arr):
            i = j = 0
            temp = []
            while i < len(left_arr) and j < len(right_arr):

                if left_arr[i] <= right_arr[j]:
                    temp.append(left_arr[i])
                    i += 1
                    
                else:
                    temp.append(right_arr[j])
                    j += 1
            
            temp.extend(left_arr[i:])
            temp.extend(right_arr[j:])
            
            return temp

        def count(left_arr, right_arr):
            nonlocal res
            for num in right_arr:
                res += bisect_right(left_arr, num + diff)

        def merge_sort(start, end):
            if start == end:
                return [nums[start]]

            mid = start + (end - start) // 2
            left_arr = merge_sort(start, mid)
            right_arr = merge_sort(mid + 1, end)

            count(left_arr, right_arr)

            return merge(left_arr, right_arr)
        
        merge_sort(0, len(nums) - 1)

        return res