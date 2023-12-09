class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

# class Solution:
#     def largestPerimeter(self, nums: List[int]) -> int:
#         perimeter = 0
#         nums.sort()
#         for i in range(3, len(nums) + 1):
#             sides = nums[i - 3:i]
#             half_perimeter = sum(sides) / 2
#             area_square = half_perimeter * (half_perimeter - sides[0]) * (half_perimeter - sides[1]) * (half_perimeter - sides[2])
#             if area_square > 0:
#                 perimeter = max(perimeter, int(half_perimeter * 2))

#         return perimeter
       

