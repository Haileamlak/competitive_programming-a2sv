# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        def get_peak(left, right):
            while left < right:
                mid = left + (right - left) // 2

                w = mountain_arr.get(mid - 1)
                x = mountain_arr.get(mid)
                y = mountain_arr.get(mid + 1)

                if w < x > y:
                    return mid

                if x < y:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        def get_target_index(left, right, reverse):
            while left <= right:
                mid = left + (right - left) // 2
                x = mountain_arr.get(mid)
                if x == target:
                    return mid
                
                if target < x:
                    if reverse:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if reverse:
                        right = mid - 1
                    else:
                        left = mid + 1

            return -1
        

        peak = get_peak(1, mountain_arr.length() - 2)

        index = get_target_index(0, peak, False)

        if index != -1:
            return index
        
        return get_target_index(peak + 1, mountain_arr.length() - 1, True)