t = int(input())    

for _ in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())

    if x1 == x2:
        print(abs(x1 - x3) ** 2)
    else:
        print(abs(x1 - x2) ** 2)