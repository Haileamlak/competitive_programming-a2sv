def transpose(matrix):
        m = len(matrix)
        n = len(matrix[0])

        transpose = []
        for i in range(n):
            transpose.append([])
            for j in range(m):
                transpose[i].append(matrix[j][i])
        
        return transpose


def isPossible(road, srow, trow, scol, tcol, n, m):
    for i in range(scol + 1, m):
        if road[srow][i] == "*":
            break
        road[srow][i] = "S"

    for i in range(scol - 1, -1, -1):
        if road[srow][i] == "*":
            break
        road[srow][i] = "S"


    for i in range(tcol + 1, m):
        if road[trow][i] == "*":
            break
        road[trow][i] = "T"

    for i in range(tcol - 1, -1, -1):
        if road[trow][i] == "*":
            break
        road[trow][i] = "T"
    
    # print(road)
    if srow == trow:
        start = min(scol, tcol)
        end = max(scol, tcol)
        for col in range(start + 1, end):
            if road[srow][col] == '*':
                break
            
        else:
            return True

    elif srow < trow:
        for col in range(m):
            if road[srow][col] == "S" and road[trow][col] == "T":
            
                for i in range(srow + 1, trow):
                    if road[i][col] == "*":
                        break
                else:
                    return True

    else:
        for col in range(m):
            if road[srow][col] == "S" and road[trow][col] == "T":
            
                for i in range(trow + 1, srow):
                    if road[i][col] == "*":
                        break
                else:
                    return True
    
    return False


nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]

srow = 0
trow = 0
scol = 0
tcol = 0
road = []
for i in range(n):
    row = [ch for ch in input()]
    if row.count('S'):
        scol = row.index("S")
        srow = i

    if row.count('T'):
        tcol = row.index("T")
        trow = i
        
    road.append(row)

road_transpose = transpose(road)

if isPossible(road, srow,trow,scol,tcol, n, m):
    print("YES")
elif isPossible(road_transpose,scol,tcol, srow, trow , m, n):
    print("YES")
else:
    print("NO")
