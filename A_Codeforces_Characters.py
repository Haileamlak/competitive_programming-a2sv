t = int(input())

for _ in range(t):
    ch = input()
    if "codeforces".find(ch) == -1:
        print("NO")
    else:
        print("YES")