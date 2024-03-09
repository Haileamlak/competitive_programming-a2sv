class SummaryRanges:

    def __init__(self):
        self.elements = []
        self.elements_set = set()

    def addNum(self, value: int) -> None:
        if value not in self.elements_set:
            bisect.insort(self.elements, value)  
            self.elements_set.add(value)

    def getIntervals(self) -> List[List[int]]:
        if not self.elements:
            return []

        res = []
        start = end = self.elements[0]
        for i in range(1, len(self.elements)):
            if self.elements[i] - end != 1:
                res.append([start, end])
                start = end = self.elements[i]
            else:
                end += 1
        
        res.append([start, end])
        return res      


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getelements()