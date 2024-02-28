for _ in range(int(input())):
    a, b, l = map(int, input().split())

    res = 0
    brek = False
    x = 0
    temp = set()
    while x > -1:
        c = (pow(a, x) * pow(b, 0) )
        if c > l:
            # brek = True
            break
        y = 0
        while y > -1:
            c = (pow(a, x) * pow(b, y) )
            if c > l:
                # brek = True
                break

            if l % (pow(a, x) * pow(b, y) ) == 0:
                res += 1
                temp.add(l // (pow(a, x) * pow(b, y) ))

            y += 1
        x += 1
        
        # if brek:
        #     break
    
    print(len(temp))