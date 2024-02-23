class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        res = []
        
        window = set()
        curr = 0
        last= -1
        for i in range(len(s)):
            if s[i] not in window:
                curr += count[s[i]]
                window.add(s[i])

            curr -= 1

            if curr == 0:
                res.append(i - last)
                last = i
                
        return res