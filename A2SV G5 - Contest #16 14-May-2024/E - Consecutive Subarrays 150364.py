# Problem: E - Consecutive Subarrays - https://codeforces.com/gym/523525/problem/E

# import sys, threading

# input = lambda: sys.stdin.readline().strip()

# def main():
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     dp = {}
    
#     def foo(i, j):
#         if (k - j) > (n - i):
#             return float('-inf')
#         if i == n:
#             if j == k:
#                 return 0
#             return float('-inf')
        
#         if (i, j) in dp:
#             return dp[(i, j)]
        
#         if j == k:
#             res = sum(a[i:]) * k
#             dp[(i, j)] = res

#         else:
#             res1 = ((a[i] * j)) + foo(i + 1, j)
#             res2 = ((a[i] * (j + 1))) + foo(i + 1, j + 1)
#             res = max(res1, res2)

#             dp[(i, j)] = res
        
#         return dp[(i, j)]
        
#     ans = a[0] + foo(1, 1)
#     print(ans)
# if __name__ == '__main__':
#     sys.setrecursionlimit(1 << 30)
#     threading.stack_size(1 << 27)

#     main_thread = threading.Thread(target=main)
#     main_thread.start()
#     main_thread.join()  

# # from math import log


# # def bc(num):
# #     return bin(num).count('1')
# #     c = 0
# #     while num:
# #         num &= (num - 1)
# #         c += 1
# #     return c

# # n, k = map(int, input().split())
# # a = list(map(int, input().split()))

# # res = float('-inf')
# # for mask in range(1 << (n - k + 1)):

    
# #     print(mask, bin(mask), k)
# #     if bc(mask) == k:
# #         t = 1
# #         curr = 0
# #         i = 0
# #         j = 1
# #         while ((1 << (j - 1)) <= mask):
# #             if mask & (1 << ( j - 1)):
# #                 # temp = mask - (mask &( mask - 1))
# #                 # print(temp)
# #                 # j = int(log(temp)) + 1
# #                 curr += sum(a[i:i + j]) * t
# #                 i += j
# #                 t += 1

# #             # mask = (mask & (mask - 1))
# #             # mask >>= 1
# #             j += 1
# #         res = max(res, curr)

# # print(res)

n, k = map(int, input().split())
nums = list(map(int, input().split()))

p = [0]* n
p[-1] = nums[-1]
for i in range(n - 2, -1, -1):
    p[i] = p[i + 1] + nums[i]

res = p[0]
temp = sorted(p[1:], reverse=True)
res += sum(temp[:k - 1])
print(res)