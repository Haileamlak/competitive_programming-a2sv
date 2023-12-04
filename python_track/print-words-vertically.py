class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_length = max(len(word) for word in words)
        res = [""] * max_length
        for i in range(max_length):
            for j in range(len(words)):
                if i > len(words[j]) - 1:
                    res[i] += " "
                else:
                    res[i] += words[j][i]
            res[i] = res[i].rstrip()
        return res
            

