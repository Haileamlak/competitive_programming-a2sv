class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_length = len(s)
        shuffled = [" " for _ in range(s_length)]
        print(len(shuffled))
        for i in range(s_length):
            shuffled[indices[i]] = s[i]

        return "".join(shuffled) 
