class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # calculate the number of operations required to move all ones in the left of the i-th position
        answer = [0 for _ in range(len(boxes))]
        num_of_ones = 0
        for i in range(1, len(boxes)):
            answer[i] = answer[i - 1] + num_of_ones
            if boxes[i - 1] == '1':
                answer[i] +=  1
                num_of_ones += 1

        # calculate the number of operations required to move all ones in the right of the i-th position and finally add that to the answer
        suffix_answer = [0 for _ in range(len(boxes))]
        num_of_ones = 0
        for i in range(len(boxes) - 2, -1, -1):
            suffix_answer[i] = suffix_answer[i + 1] + num_of_ones
            if boxes[i + 1] == '1':
                suffix_answer[i] += 1
                num_of_ones += 1
            
            answer[i] += suffix_answer[i]
        
        return answer
