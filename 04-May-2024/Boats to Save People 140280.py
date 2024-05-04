# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()

        res = 0

        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                
            res += 1
            right -= 1
        
        return res