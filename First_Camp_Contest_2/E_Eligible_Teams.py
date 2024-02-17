for _ in range(int(input())):
    n, x = map(int, input().split())
    skill = list(map(int, input().split()))
    skill.sort(reverse=True)

    res = 0
    i = 0
    while i < n:
        j = 1
        while i < n and (skill[i] * j) < x:
            i += 1
            j += 1
        
        if i < n:
            res += 1
        i += 1
    
    print(res)
