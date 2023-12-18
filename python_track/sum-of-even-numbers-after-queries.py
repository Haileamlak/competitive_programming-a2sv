class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum = 0
        for num in nums:
            if num % 2 == 0:
                sum += num
        
        answer = [0 for _ in range(len(queries))]
        for i in range(len(queries)):
            index = queries[i][1]
            val = queries[i][0]
            
            if nums[index] % 2 == 0:
                sum -= nums[index]

            nums[index] += val
            if nums[index] % 2 == 0:
                sum += nums[index]
            
            answer[i] = sum

        return answer

            