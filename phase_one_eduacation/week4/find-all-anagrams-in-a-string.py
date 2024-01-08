class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []

        word = defaultdict(int)
        temp = defaultdict(int)
        for i in range(len(p)):
            word[p[i]] += 1
            temp[s[i]] += 1

        res = []
        if word == temp:
            res.append(0)

        for i in range(len(p), len(s)):
            temp[s[i]] += 1
            temp[s[i - len(p)]] -= 1
            if temp[s[i - len(p)]] == 0:
                del temp[s[i - len(p)]]

            if word == temp:
                res.append(i - len(p) + 1)
            
        
        return res
        