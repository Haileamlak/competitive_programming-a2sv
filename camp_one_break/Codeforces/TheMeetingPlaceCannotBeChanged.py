n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))
 
def possible_to_meet(time):
    temp = [1, pow(10, 9)]
    for i in range(n):
        temp[0] = max(temp[0], x[i] - time * v[i])
        temp[1] = min(temp[1], x[i] + time * v[i])
    
    return temp[0] <= temp[1]
 
minT = 0
maxT = max(x)
while maxT - minT > pow(10, -6):
    midT = minT + (maxT - minT) / 2
    if possible_to_meet(midT):
        maxT = midT - pow(10, -6)
    else:
        minT = midT + pow(10, -6)
 
print(minT)