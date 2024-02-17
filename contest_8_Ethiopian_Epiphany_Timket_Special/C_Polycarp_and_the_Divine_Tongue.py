t = int(input())

for _ in range(t):
    word = input()

    res = 0
    win = 0
    for i in range(len(word)):
        if word[i] == 'w':
            res += 1
            res += win // 2
            win = 0
        else:
            win += 1
    
    res += win // 2
    print(res)