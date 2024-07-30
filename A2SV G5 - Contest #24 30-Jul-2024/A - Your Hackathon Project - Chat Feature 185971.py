# Problem: A - Your Hackathon Project - Chat Feature - https://codeforces.com/gym/534160/problem/A

for i in range(int(input())):
    n = int(input())
    w = input()
    j = n - 1
    while j >= 0 and w[j] == ')':
        j -= 1
    
    if n - j - 1  > n // 2:
        print('YES')
    else:
        print('NO')