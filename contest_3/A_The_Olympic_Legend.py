t = int(input())

for _ in range(t):
    runs = list(map(int, input().split()))

    kenenisa = runs[0]
    count = 0
    for i in range(1, 4):
        if runs[i] > kenenisa:
            count += 1
    
    print(count)