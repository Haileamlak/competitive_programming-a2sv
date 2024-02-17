class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        # self.stream = deque()
        self.correct = 0        

    def consec(self, num: int) -> bool:
        # if len(self.stream) == self.k and self.stream.popleft() == self.value:
        #     self.correct -= 1

        if num == self.value:
            self.correct += 1
        else:
            self.correct = 0
            
        
        # self.stream.append(num)
        
        return (self.correct >= self.k)


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)