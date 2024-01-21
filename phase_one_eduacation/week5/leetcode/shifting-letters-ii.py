class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        def shift_letter(letter, shift):
            res = ord(letter) + (shift % 26)
            if res < 97:
                res += 26
            elif res > 122:
                res -= 26

            return chr(res)

        n = len(s)
        pre_sum = [0 for _ in range(n + 1)]
        for shift in shifts:
            if shift[2] == 0:
                pre_sum[shift[0]] -= 1
                pre_sum[shift[1] + 1] += 1
            else:
                pre_sum[shift[0]] += 1
                pre_sum[shift[1] + 1] -= 1
        
        for i in range(1, n):
            pre_sum[i] += pre_sum[i - 1]

        res = [letter for letter in s]
        for i in range(n):
            res[i] = shift_letter(res[i], pre_sum[i])

        return ''.join(res)

        