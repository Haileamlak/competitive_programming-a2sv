n = int(input())

# names = ["" for _ in range(n)]
# nums = [[] for _ in range(n)]
res = []
for i in range(n):
    inpt =  input().split() # list(map(str, input().split()))
    # print(inpt)
    m = float("{:.3f}".format(int(inpt[2]) * 2))
    p = float("{:.3f}".format(int(inpt[3] )* 3/2))
    rest = sum(list(map(int, inpt[4:] )))
    temp =float("{:.3f}".format((m + p + rest) * 100 / 195)) 
    x = (int(inpt[1]) / 7 * 4 / 10)  +  temp * 6/ 10
    # for i in range(2, 7)
    # +  (sum(list(map(int, inpt[2:]))) * 2 / 3)
    # print(x)
    res.append((inpt[0], float(x)))


res.sort(key=lambda x:x[0])
res.sort(reverse=True, key=lambda x:x[1])

# res.sort(key=lambda x: if x[1] == x[2])
print(res)
for i in range(n):
    print(res[i][0], "{:.3f}".format(res[i][1]))

# 5
# N 650 24 25 17 29 30
# Y 590 23 28 27 29 26
# A 650 24 25 20 29 27
# J 600 21 23 10 13 16
# N 540 30 22 18 19 20