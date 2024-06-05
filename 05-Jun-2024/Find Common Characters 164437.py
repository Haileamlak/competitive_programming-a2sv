# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = [Counter(word) for word in words]

        res = []
        for letter in ascii_lowercase:
            res.extend([letter] * min(word_count[letter] for word_count in count))

        return res