t = int(input())

for _ in range(t):
    n = int(input())
    row1 = input()
    row2 = input()
    for i in range(n):
        if (row1[i] == 'R' and row2[i] != 'R') or ((row1[i] == 'G' or row1[i] == 'B') and row2[i] == 'R'):
            print('NO')
            break
    else:
        print("YES")            
        