class Solution:
    def numberOfWays(self, s: str) -> int:
        total_count = []
        left_count = []
        right_count = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                total_count.append(count)
                left_count.append(count)
                right_count.append(count)
                count = 1

        total_count.append(count)
        left_count.append(count)
        right_count.append(count)
        
        for i in range(2, len(left_count), 2):
            left_count[i] += left_count[i - 2]
        
        for i in range(3, len(left_count), 2):
            left_count[i] += left_count[i - 2]

        # start = len(total_count) % 2
        for i in range(len(right_count) - 3, -1, -2):
            right_count[i] += right_count[i + 2]

        for i in range(len(right_count) - 4, -1, -2):
            right_count[i] += right_count[i + 2]


        result = 0
        for i in range(1, len(total_count) - 1):
            result += (left_count[i - 1] * total_count[i] * right_count[i + 1])
        
        return result



