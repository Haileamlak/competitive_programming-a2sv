class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutive(answerKey, k, answer):
            left = 0
            longest = 0
            length = 0
            for right in range(len(answerKey)):
                if answerKey[right] == answer:
                    length += 1
                
                currWindow = right - left + 1
                if currWindow - length > k:
                    if answerKey[left] == answer:
                        length -= 1
                    left += 1
                
                else:
                    longest = max(longest, currWindow)
            
            return longest

        true = maxConsecutive(answerKey, k, 'T')
        false = maxConsecutive(answerKey, k, 'F')
        return max(true, false)