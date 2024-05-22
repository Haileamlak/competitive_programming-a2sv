# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station = self.check_in[id][0]
        start_time = self.check_in[id][1]
        if (start_station, stationName) in self.time:
            self.time[(start_station, stationName)][0] += (t - start_time)           
            self.time[(start_station, stationName)][1] += 1
        else:
            self.time[(start_station, stationName)] = [t - start_time, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.time[(startStation, endStation)][0] / self.time[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)