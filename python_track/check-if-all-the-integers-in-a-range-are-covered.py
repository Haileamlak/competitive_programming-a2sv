class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges_set = set()
        for aRange in ranges:
            ranges_set.update([num for num in range(aRange[0], aRange[1] + 1)])
        
        required_set = set([i for i in range(left, right + 1)])
        
        return required_set <= ranges_set