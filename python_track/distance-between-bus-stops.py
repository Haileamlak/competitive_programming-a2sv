class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        length1 = 0
        i = start
        while i != destination:
            length1 += distance[i]
            i = (i + 1) % len(distance)

        length2 = 0
        while i != start:
            length2 += distance[i]
            i = (i + 1) % len(distance)

        return min(length1, length2)
