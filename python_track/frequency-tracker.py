class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.count = defaultdict(int) 

    def add(self, number: int) -> None:
        freq = self.freq[number]
        self.freq[number] += 1

        self.count[freq] -= 1
        if self.count[freq] <= 0:
            del self.count[freq]
        
        self.count[freq + 1] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.freq:
            freq = self.freq[number]
            if freq > 1:
                self.freq[number] -= 1
            else:
                del self.freq[number]
            
            self.count[freq] -= 1

            if self.count[freq] <= 0:
                del self.count[freq]
                
            self.count[freq - 1] += 1
            
    def hasFrequency(self, frequency: int) -> bool:
        # for freq in self.freq.values():
        #     if freq == frequency:
        #         return True
        
        # return False
        return self.count[frequency] > 0 


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)