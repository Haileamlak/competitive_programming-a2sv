left, right = map(int, input().split())

for i in range(left, right + 1):  
    num = str(i)      
    if len(set(num)) == len(num):
        print(i)
        break
else:
    print(-1)