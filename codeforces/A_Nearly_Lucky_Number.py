n = input()

res = 0

for num in n:
    if num == '4' or num == '7':
        res += 1

if res == 4 or res == 7:
    print("YES")
else:
    print("NO")