class OrderedStream:

    def __init__(self, n: int):
        self.values = ["" for _ in range(n)]
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.values[idKey] = value
        res = []
        if idKey == self.ptr:
            while self.ptr < len(self.values) and self.values[self.ptr] != '':
                res.append(self.values[self.ptr])
                self.ptr += 1
        return res
        



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)