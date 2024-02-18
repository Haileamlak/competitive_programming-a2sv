for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print(2)
        print(1, 2)
    else:
        print(2)
        print(n -2, n)
        temp = (n + n - 2) // 2

        print(temp, n - 1)
        for i in range(n - 3, 0,-1):
            print( temp, i )
            temp = (temp + i) // 2