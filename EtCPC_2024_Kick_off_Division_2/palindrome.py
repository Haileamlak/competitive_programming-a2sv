from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    
    temp = Counter(input())
    del temp[' ']

    one = False
    for val in temp.values():
        # if val == 1:
        #     if one:
        #         print("NO")
        #         break
        #     else:
        #         one = True
        if val % 2 == 1:
            if one:
                print("NO")
                break
            else:
                one = True
    
    else:
        print("YES")
