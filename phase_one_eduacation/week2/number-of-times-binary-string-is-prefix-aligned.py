class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_fliped = 0
        count = 0
        for i in range(len(flips)):
            max_fliped = max(max_fliped, flips[i] - 1)

            if i == max_fliped:
                count += 1

        return count