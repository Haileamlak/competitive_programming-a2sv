from collections import Counter
for _ in range(int(input())):
    n = int(input())
    word = input()
    count = Counter(word)

    res = n + 1
    if count['a'] > count['b'] and count['a'] > count['c']:
        res = 2
    
    # l = 0
    # for r in range(2, n):
    #     count[word[r]] += 1

    #     while ( r - l + 1) >= 2 and (count['a'] > count['b'] and count['a'] > count['c']):
    #         res = min(res, r - l + 1)
    #         count[word[l]] -= 1
    #         l += 1
    
    # if res == n + 1:
    #     print(-1)
    # else:
    #     print(res)
    
    l = 0 
    r = n - 1
    while r - l + 1 >= 2:
        if word[l] == 'a' and word[r] == 'a':
            if count['a'] > count['b'] and count['a'] > count['c']:
                res = 2
            res = min(res, r - l + 1)
            count['a'] -= 2
            l += 1
            r -= 1
        else:
            if word[r] ==  'c' or word[r] == 'b':
                count[word[r]] -= 1
                r -= 1
            if word[l] == 'c' or word[l] == 'b':
                count[word[l]] -= 1
                l += 1

    
    if r == n + 1:
        print(-1)
    else: 
        print(res)