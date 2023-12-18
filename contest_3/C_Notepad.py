t = int(input())

for _ in range(t):
    n = int(input())
    word = input()

    possible = False
    i = 0
    for i in range(n - 1):
        if word[i:i+2] in word[i+2:]:
            print("YES")
            break
    else:
        print("NO")