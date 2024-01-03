class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s.sort()
        g.sort()
        
        count = 0

        first = 0
        second = 0
        while first < len(g) and second < len(s):
            if s[second] >= g[first]:
                count += 1

                second += 1
                first += 1

            else:
                second += 1
        
        return count
        