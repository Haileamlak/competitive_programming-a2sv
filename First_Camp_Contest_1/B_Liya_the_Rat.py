word = input()
res = [0] * (len(word) - 1)
for i in range(len(word) - 1):
    if  word[i] == word[i + 1]:
        res[i] = 1
    
    if i > 0:
        res[i] += res[i - 1]
    
    
    
# for i in range(1, len(word)):
#     res[i] += res[i - 1]



# print(res)
    

for i in range(int(input())):
    l, r = map(int, input().split())

    ans = 0
    if r > 1:
        ans = res[r - 2]
    # else:

    if l > 1:
        ans -= res[l - 2]
    
    print(ans)
