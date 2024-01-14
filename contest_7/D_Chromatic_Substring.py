from math import ceil


t = int(input())

def differ(a, b):
    res = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            res += 1
    
    return res

def help(word, n, k, a):
    res = differ(word[0:k], a)
    # win = [word[i] for i in range(k)]
    temp = res
    for i in range(k, n):
        if word[i - k] == a[i - k]:
           temp -= 1
        # win.pop(0)
        # win.append(word[i])
        if word[i] == a[i]:
            temp += 1

        res = max(res, temp)
    
    return res

for _ in range(t):
    n, k = map(int, input().split())
    word = input()
    r = 'RGB' * ceil(n / 3)
    g = 'GBR' * ceil(n / 3)
    b = 'BRG' * ceil(n / 3)
    # if n % 3 == 1:
    #     r += 'R'
    #     g += 'G'
    #     b += 'B'
    # elif n % 3 == 2:
    #     r += 'RG'
    #     g += 'GB'
    #     b += 'BR'
    
    res1 = help(word, n, k, r)
    res2 = help(word, n, k, g)
    res3 = help(word, n, k, b)
    res = max(res1, res2, res3)

    print(k - res)

