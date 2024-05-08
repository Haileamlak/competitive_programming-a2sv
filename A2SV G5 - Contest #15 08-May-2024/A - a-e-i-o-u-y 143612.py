# Problem: A - a-e-i-o-u-y - https://codeforces.com/gym/522079/problem/A

n = int(input())
word = input()

res= []

for i in range(n):
    if not res or res[-1] not in 'aeiouy' or word[i] not in 'aeiouy':
        res.append(word[i])
#     while res and
# i = 0
# while i < len(word) and (not res or res[-1] not in 'aeiouy'):
#     res.append(word[i])
#     i += 1

# index = i

# # ans = word
# for t in range(len(word) - 2, -1, -1):
#     if word[t] in 'aeiouy' and word[t + 1] in 'aeiouy':
#         flag = False
#         for j in range(index, t + 1):
#             if word[j] not in 'aeiouy':
#                 res.append(word[j])
#             else:
#                 flag = True
#         if flag and res[-1] not in 'aeiouy':
#             res.append(word[t + 1])

#         res += list(word[t + 2:])
        
#         break
#     if t == index - 1:
#         res += list(word[t + 1:])
#         break
# # for j in range(i, n):
# #     if word[j] in 'aeiouy' and (res and res[-1] in 'aeiouy'):
# #         deleted = res[:index]
# #         # flag = False
# #         for k in range(index, len(res)):
# #             if res[k] not in 'aeiouy':
# #                 deleted.append(res[k])
# #             # else:
# #             #     flag = True
        
# #         res = deleted.copy()
# #         if res and res[-1] not in 'aeiouy':    
# #             res.append(word[j])
# #     else:
# #         res.append(word[j])


print(''.join(res))