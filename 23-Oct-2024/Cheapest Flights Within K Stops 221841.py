# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k + 1):
            temp = prices[:]
            
            for u, v, p in flights:
                temp[v] = min(temp[v], prices[u] + p)
        
            prices = temp

        return prices[dst] if prices[dst] != float('inf') else -1