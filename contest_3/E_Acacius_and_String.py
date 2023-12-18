t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = [s[i] for i in range(n)]

    abs = "abacaba"
    index = set()
    count = 0
    possible = False

    for i in range(n - 6):
        word = s[i:i+7]
        unused = 0
        already = 0
        for j in range(7):

            if word[j] == abs[j]:
                already += 1

            elif word[j] == '?':
                if not possible:
                    res[i + j] = abs[j]
                    index.add(i + j)
                else:
                    res[i+j] = 'd'

            else:
                unused += 1
        
        if already == 7:
            count += 1

        elif unused == 0:
            possible = True

    if count == 1:
        
        if possible:
            for idx in index:
                res[idx] = 'd'

        print("Yes")
        print(''.join(res))
        
    elif count == 0 and possible:
        print("Yes")
        print(''.join(res))
    else:
        print("No")
    