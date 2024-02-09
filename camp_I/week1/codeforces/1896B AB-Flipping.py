for _ in range(int(input())):
    n = int(input())
    word = input()

    b = 0
    res = 0
    for i in range(n - 1, -1, -1):
        if word[i] == 'B':
            b += 1
        
        else:
            res += b  
            b = int(bool(b))

    print(res)