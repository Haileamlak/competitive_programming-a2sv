t = int(input())

for _ in range(t):
    n = int(input())
    grid = []
    for i in range(n):
        row = input()
        grid.append([int(ch) for ch in row])

    # print(grid)
    i = 0
    n -= 1
    count = 0
    while(i < n):
        a = [i, i]
        b = [i, n]
        c = [n, n]
        d = [n, i]

        while a[1] < n:

            total = grid[a[0]][a[1]] + grid[b[0]][b[1]] + grid[c[0]][c[1]] + grid[d[0]][d[1]]

            if total == 2:
                count += 2
            elif total == 1 or total == 3:
                count += 1

            a[1] += 1
            b[0] += 1
            c[1] -= 1
            d[0] -= 1

        i += 1
        n -= 1
    
    print(count)

    