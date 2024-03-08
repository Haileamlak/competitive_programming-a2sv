class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        def isvalid(window, forbidden_set):
            for i in range(1, 11):
                curr = window[len(window) - i:]
                if curr in forbidden_set:
                    return i
            return 0

        forbidden_set = set(forbidden)
        longest = 0
        left  = 0
        window = ''
        for right in range(len(word)):
            window += word[right]
            idx = isvalid(window, forbidden_set)
            if idx:
                window = window[len(window) - idx + 1:]
                left = right - idx + 2

            longest = max(longest, right - left + 1)
        
        return longest