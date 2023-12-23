# t = int(input())

# for _ in range(t):
#     nm = list(map(int, input().split()))

#     n = nm[0]
#     m = nm[1]

#     chess = []
#     for i in range(n):
#         row = list(map(int, input().split()))
#         chess.append(row)
    
#     diag1 = [0 for _ in range(n + m - 1)]
#     diag2 = [0 for _ in range(n + m - 1)]

#     for row in range(n):
#         i = row
#         j = 0
        
#         score = 0
#         while i < n and j < m:
#             score += chess[i][j]

#             i += 1
#             j += 1
        
#         diag1[row] = score
    
#     for col in range(1, m):
#         i = 0
#         j = col

#         score = 0
#         while i < n and j < m:
#             score += chess[i][j]

#             i += 1
#             j += 1
        
#         diag1[n + col - 1] = score


#     for row in range(n):
#         i = row
#         j = m - 1
        
#         score = 0
#         while i >= 0 and j >= 0:
#             score += chess[i][j]

#             i -= 1
#             j -= 1
        
#         diag2[row] = score
    
#     for col in range(0, m - 1):
#         i = 0
#         j = col

#         score = 0
#         while i >= 0 and j >= 0:
#             score += chess[i][j]

#             i -= 1
#             j -= 1
        
#         diag2[n + col] = score

    
#     # diag1.sort(reverse=True)
#     # diag2.sort(reverse=True)

#     # print(diag1[0] + diag2[0] - 1)

    




#     max_score = 0
#     for row in range(n):
#         for col in range(m):
#             score1 = 0
#             if row <= col:
#                 score1 = diag1[row]
#             else:
#                 score1 = diag1[n - 1 + col - row]

#             if row > n // 2:
#                 score2 = diag2[n + row]
#             else:
#                 score2 = diag2[n - 1 - row]

#             max_score = max(max_score, score1 + score2 - chess[row][col]) 
    
#     print(max_score)


t = int(input())
 
for _ in range(t):
    nm = list(map(int, input().split()))
 
    n = nm[0]
    m = nm[1]
 
    chess = []
    for i in range(n):
        row = list(map(int, input().split()))
        chess.append(row)
    
    max_score = 0
    for row in range(n):
        for col in range(m):
            score = chess[row][col]
 
            i = row - 1
            j = col - 1
 
            while i >= 0  and j >= 0:
                score += chess[i][j]
 
                i -= 1
                j -= 1
 
            i = row + 1
            j = col + 1
 
            while i < n  and j < m:
                score += chess[i][j]
 
                i += 1
                j += 1
            
            i = row - 1
            j = col + 1
 
            while i >= 0  and j < m:
                score += chess[i][j]
 
                i -= 1
                j += 1
 
            i = row + 1
            j = col - 1
 
            while i < n  and j>= 0:
                score += chess[i][j]
 
                i += 1
                j -= 1
            
            max_score = max(max_score, score)
    
    print(max_score)