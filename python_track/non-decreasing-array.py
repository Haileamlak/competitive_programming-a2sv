# class Solution:
#     def checkPossibility(self, nums: List[int]) -> bool:
#         yet = False
#         num = pow(-10, 5)
#         for i in range(len(nums)):
#             # if nums[i] > nums[i + 1]:
#             #     if  not yet:
#             #         yet = True
#             #     else:
#             #         return False
#             if nums[i] < num:
#                 if  not yet:
#                     yet = True
#                 else:
#                     yet = False
#                     break
#             else:
#                 num = nums[i]
        
#         yet_back = False
#         num = pow(10, 5)
#         for i in range(len(nums) - 1, -1, -1):
#             # if nums[i] > nums[i + 1]:
#             #     if  not yet:
#             #         yet = True
#             #     else:
#             #         return False
#             if nums[i] > num:
#                 if  not yet_back:
#                     yet_back = True
#                 else:
#                     yet_back = False
#                     break
#             else:
#                 num = nums[i]
            

#         return yet or yet_back
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if count == 1:
                    return False
                
                count += 1

                if (i - 2) >= 0 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]

        
        return True