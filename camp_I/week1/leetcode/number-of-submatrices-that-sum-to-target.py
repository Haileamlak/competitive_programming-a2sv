class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # calculate the prefix sum for each row only
        for row in range(m):
            for col in range(1, n):
                matrix[row][col] += matrix[row][col - 1]

        count = 0
        for col1 in range(n):
            for col2 in range(col1, n):
                print(col1, col2)
                count_prefix = defaultdict(int)
                count_prefix[0] = 1

                window_sum = 0

                for row in range(m):
                    window_sum += matrix[row][col2]

                    if col1 > 0:
                        window_sum -= matrix[row][col1 - 1]
                    
                    count += count_prefix[window_sum - target]
                    count_prefix[window_sum] += 1
        
        return count