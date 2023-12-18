class Bitset:

    def __init__(self, size: int):
        self.bits = ['0' for _ in range(size)]
        self.ones = 0
        self.flips = 0

    def fix(self, idx: int) -> None:
        if self.flips % 2 == 0:
            if self.bits[idx] == '0':
                self.bits[idx] = '1'
                self.ones += 1
        else:
            if self.bits[idx] == '1':
                self.bits[idx] = '0'
                self.ones += 1

    def unfix(self, idx: int) -> None:
        if self.flips % 2 == 0:
            if self.bits[idx] == '1':
                self.bits[idx] = '0'
                self.ones -= 1

        else:
            if self.bits[idx] == '0':
                self.bits[idx] = '1'   
                self.ones -= 1

    def flip(self) -> None:
        self.flips += 1
        self.ones = len(self.bits) - self.ones

    def all(self) -> bool:
        return self.ones == len(self.bits) 

    def one(self) -> bool:
        return self.ones >= 1

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        if self.flips % 2 == 0:
            return ''.join(self.bits)
        temp = list(map(lambda x:'0' if x == '1' else '1', self.bits))
        return ''.join(temp) 
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()