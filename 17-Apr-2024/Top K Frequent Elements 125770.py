# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class MyTuple:
    def __init__(self, _tuple):
        self._tuple = _tuple
    
    def __lt__(self, other):
        return self._tuple[1] < other[1]

    def __getitem__(self, index):
        return self._tuple[index]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [MyTuple((i, cnt)) for i, cnt in count.items()]
        
        heapify(freq)

        return [num[0] for num in heapq.nlargest(k, freq)]