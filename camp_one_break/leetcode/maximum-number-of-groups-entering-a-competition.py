class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort()
        
        res = 0
        prev_count = 0
        prev_sum = 0
        curr_sum = 0
        count = 0
        for grade in grades:
            curr_sum += grade
            count += 1

            if curr_sum > prev_sum and count > prev_count:
                prev_sum = curr_sum
                prev_count = count
                curr_sum = 0
                count = 0
                res += 1
        
        return res