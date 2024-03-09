class TimeMap:

    def __init__(self):
        self.key_value = {}
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_value:
            self.key_value[key] = []
        
        bisect.insort(self.key_value[key], timestamp)

        self.values[(key, timestamp)] = value


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_value:
            return ''

        if (key, timestamp) in self.values:
            return self.values[(key, timestamp)]
        
        timestamps = self.key_value[key]

        index = bisect_left(timestamps, timestamp)

        if index == 0:
            return ''

        return self.values[(key, timestamps[index - 1])]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)