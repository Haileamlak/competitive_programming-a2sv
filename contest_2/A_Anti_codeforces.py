t = int(input())

for _ in range(t):
    word = input()
    res = 0
    for i in range(len(word)):
        if "codeforces"[i] != word[i]:
            res += 1
    print(res)