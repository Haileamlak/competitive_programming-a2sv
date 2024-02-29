class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
            
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combinations = []
        combination = []

        def back_track(index):
            if index == len(digits):
                combinations.append("".join(combination))
                return

            key = letters[digits[index]]
            for i in range(len(key)):
                combination.append(key[i])
                back_track(index + 1)
                combination.pop()


        back_track(0)
        return combinations
