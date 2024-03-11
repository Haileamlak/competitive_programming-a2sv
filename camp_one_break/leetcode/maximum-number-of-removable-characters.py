class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        removable_map = {}
        for index in range(len(removable)):
            removable_map[removable[index]] = index + 1

        def is_subsequence_with(k):
            p_ptr = 0
            for s_ptr in range(len(s)):
                if (s_ptr not in removable_map or removable_map[s_ptr] > k) and s[s_ptr] == p[p_ptr]:
                    p_ptr += 1
                
                if p_ptr == len(p):
                    return True

            return False
            # while s_ptr < len(s) and p_ptr < len(p): 
            #     while s_ptr < len(s) and ((s_ptr in removable_map and removable_map[s_ptr] <= k) or s[s_ptr] != p[p_ptr]):
            #         s_ptr += 1
            #     if s_ptr < len(s):
            #         p_ptr += 1
            #         # return False
            
        
        min_k, max_k = 0, len(removable)
        ans = 0
        while min_k <= max_k:
            mid_k = min_k + (max_k - min_k) // 2
            if is_subsequence_with(mid_k):
                min_k = mid_k + 1
            else:
                max_k = mid_k - 1
        
        return max_k