class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        def num_of_soldiers(row):
            left, right = 0, len(mat[row]) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if mat[row][mid] == 1:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return right
        
        res = list(range(len(mat)))

        res.sort(key = lambda row : (num_of_soldiers(row), row))
        
        return res[:k]