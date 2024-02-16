class RecentCounter:

    def __init__(self):
        self.count = 0
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.count += 1

        while self.requests[0] < t - 3000:
            self.count -= 1
            self.requests.pop(0)
        
        
        return self.count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)