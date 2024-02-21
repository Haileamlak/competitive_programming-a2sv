class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        total = sum(nums)

        def calculate(left, right, isPlayer1):
            if left == right:
                if isPlayer1:
                    return nums[left]

                return 0

            ans1 = 0
            ans2 = 0

            if isPlayer1:
                ans1 += nums[left]
                ans2 += nums[right]
                
            ans1 += calculate(left + 1, right, not isPlayer1)
            ans2 += calculate(left, right - 1, not isPlayer1)

            return max(ans1, ans2) if isPlayer1 else min(ans1, ans2)
            
            
        x = calculate(0, len(nums) - 1, True)
        return x >= (total - x)