# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []

        for word in words:
            mapp = {}
            used = {}
            for letter, ch in zip(word, pattern):
                if letter not in mapp and ch not in used:
                    mapp[letter] = ch
                    used[ch] = letter
                elif letter not in mapp or ch not in used:
                    break
                elif mapp[letter] != ch or used[ch] != letter:
                    break

            else:
                res.append(word)

        return res