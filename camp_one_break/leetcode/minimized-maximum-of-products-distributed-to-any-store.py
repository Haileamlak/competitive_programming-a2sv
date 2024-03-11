class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def number_of_stores(num):
            res = 0
            for quantity in quantities:
                res += ceil(quantity / num)
            
            return res
        
        min_quantity = 1
        max_quantity = max(quantities)
        while min_quantity <= max_quantity:
            mid = min_quantity + (max_quantity - min_quantity) // 2
            if number_of_stores(mid) <= n:
                max_quantity = mid - 1
            else:
                min_quantity = mid + 1
        
        return min_quantity