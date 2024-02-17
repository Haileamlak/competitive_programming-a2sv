t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    word = input()


    win = 0
    for i in range(k):
        if word[i] == 'W':
            win += 1

    res = win
    for i in range(k, len(word)):
        if word[i] == 'W':
            win += 1
        if word[i - k] == 'W':
            win -= 1
        
        res = min(res, win)
    
    print(res)