class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index = {nums[i]:i for i in range(len(nums))}

        for i in range(len(operations)):
            nums[index[operations[i][0]]] = operations[i][1]
            index[operations[i][1]] = index[operations[i][0]]
            index.pop(operations[i][0])
        
        return nums