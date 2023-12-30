n = int(input())
temp = []
for i in range(n):
    temp.append(input())

temp.sort(key=lambda x:len(x))

for i in range(n - 1):
    if temp[i] not in temp[i + 1]:
        print("NO")
        break
else:
    print("YES")
    for tt in temp:
        print(tt)