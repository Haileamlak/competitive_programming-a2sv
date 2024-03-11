class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        count = Counter(s)
        for letter in order:
            if letter in count:
                res += [letter] * count[letter]
                count.pop(letter)
        
        for letter in count:
            res += [letter] * count[letter]
        
        return ''.join(res)