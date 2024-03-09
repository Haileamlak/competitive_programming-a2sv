class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        left, right = 0, len(self.intervals) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.intervals[mid][0] <= value <= self.intervals[mid][1]:
                return
            elif self.intervals[mid][0] > value:
                right = mid - 1
            else:
                left = mid + 1            
        if left == len(self.intervals):
            if self.intervals and self.intervals[-1][1] + 1 == value:
                self.intervals[-1][1] = value
            else:
                self.intervals.append([value, value])
        elif left == 0:
            if self.intervals and self.intervals[0][0] - 1 == value:
                self.intervals[0][0] = value
            else:
                self.intervals.insert(0, [value, value])
        else:
            if self.intervals[left - 1][1] + 1 == value and self.intervals[left][0] - 1 == value:
                self.intervals[left - 1][1] = self.intervals[left][1]
                self.intervals.pop(left)
            elif self.intervals[left - 1][1] + 1 == value:
                self.intervals[left - 1][1] = value
            elif self.intervals[left][0] - 1 == value:
                self.intervals[left][0] = value
            else:
                self.intervals.insert(left, [value, value])
        


    def getIntervals(self) -> List[List[int]]:
        return self.intervals        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()