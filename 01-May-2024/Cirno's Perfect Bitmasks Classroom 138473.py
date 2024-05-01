# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

for i in range(int(input())):
    x = int(input())

    if x == 1:
        print(3)
        
    elif x & (x - 1) == 0:
        print(x + 1)
    else:
        i = 0
        while (1 << i) & x == 0:
            i += 1
        
        print(1 << i)