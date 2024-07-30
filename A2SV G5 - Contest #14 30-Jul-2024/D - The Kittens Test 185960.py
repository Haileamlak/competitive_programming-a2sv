# Problem: D - The Kittens Test - https://codeforces.com/gym/520688/problem/D

n = int(input())

p = {i:i for i in range(1, n + 1)}
left = {i:i for i in range(1, n + 1)}
right = {i:i for i in range(1, n + 1)}

def get(x):
    a = x
    while a != p[a]:
        a = p[a]

    while x != p[x]:
        temp = p[x]
        p[x] = a
        x = temp

    return a
# def get2(x):
#     a = x
#     while a != tail[a]:
#         a = tail[a]
#     # while x != p[x]:
#     #     temp = p[x]
#     #     p[x] = a
#     #     x = temp
#     return a

def union(x, y):
    px, py = get(x), get(y)
    if px != py:
        lx = left[px]
        rx = right[px]
        ly = left[py]
        ry = right[py]
        left[ly] = rx
        # left[px] = ly
        right[px] = ry

        p[py] = px
        # tail[py] = tail[px]
        # left[right[py]] = x
        # left[py] = x


for _ in range(n - 1):
    a, b = map(int, input().split())
    union(a, b)
# print(tail, p)
temp = right[get(1)]
while temp != left[temp]:
    print(temp, end= ' ')
    temp = left[temp]

# print(left, right)
print(temp)