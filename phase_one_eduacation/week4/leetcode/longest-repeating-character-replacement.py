class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        frequent = 0
        left = 0
        res = 0
        for right in range(len(s)):
            frequency[s[right]] += 1
            frequent = max(frequent, frequency[s[right]])

            window_size = right - left + 1
            if window_size - frequent > k:
                frequency[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res