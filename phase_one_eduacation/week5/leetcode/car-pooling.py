class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        start = trips[0][1]
        end = trips[0][2]
        for trip in trips:
            start = min(start, trip[1])
            end = max(end, trip[2])

        # trips.sort(key=lambda x:x[2])
        temp = [0 for _ in range(end - start + 1)]
        for trip in trips:
            temp[trip[1] - start] += trip[0]
            temp[trip[2] - start] -= trip[0]

        if temp[0] > capacity:
            return False

        for i in range(1, len(temp)):
            temp[i] += temp[i - 1]
            if temp[i] > capacity:
                return False
        
        print(temp)
        return True