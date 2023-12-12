class Solution:
    def spaces_only(self, input_str):
        return all(char.isspace() for char in input_str)

    def reverseWords(self, s: str) -> str:
        s_arr = s.strip().split(' ')
        words_only = lambda word: not self.spaces_only(word)
        s_arr = list(filter(words_only, s_arr))
        end = len(s_arr) - 1
        start = 0
        while start < end:
            s_arr[start], s_arr[end] = s_arr[end], s_arr[start]
            start += 1
            end -= 1

        return ' '.join(s_arr)
