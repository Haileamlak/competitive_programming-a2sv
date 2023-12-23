
nm = list(map(int, input().split()))

n = nm[0]
m = nm[1]

road = []
for i in range(n):
    row = input()
    # line = [ch for ch in row]
    road.append(row)

# print(road
openrow = [0, m]

srow = 0
trow = 0

for i in range(n):
    if road[i].count("S"):

        col = road[i].index("S")
        srow = i

        while col >= 0 and road[i][col] != '*':
            col -= 1

        col += 1
        openrow[0] = max(col, openrow[0])

        while col < m and road[col] != '*':
            col += 1
        
        openrow[1] = min(col - 1, openrow[1])
    
    elif road[i].count('T'):

        col = road[i].index("T")
        trow = i

        while col >= 0 and road[i][col] != '*':
            col -= 1

        col += 1
        openrow[0] = max(col, openrow[0])
        while col < m and road[col] != '*':
            col += 1
        
        openrow[1] = min(col - 1, openrow[1])


st = min(srow, trow)
en = max(srow, trow)

for i in range(openrow[0], openrow[1] + 1):
    cnt = 0
    for j in range(st, en + 1):
        if road[i][j] == '*':
            cnt -= 1

    if cnt == 0:
        print("YES")
        break
else:
    print("NO")





