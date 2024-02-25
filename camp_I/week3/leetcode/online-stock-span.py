class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []


    def next(self, price: int) -> int:
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()
        
        previous_large = -1 if not self.stack else self.stack[-1]

        self.prices.append(price)

        i = len(self.prices) - 1

        self.stack.append(i)

        return i - previous_large


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)