# Problem: B - tourist orz! - https://codeforces.com/gym/522079/problem/B

for i in range(int(input())):
    n, z = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0
    for num in a:
        res = max(res, num | z)

    print(res)