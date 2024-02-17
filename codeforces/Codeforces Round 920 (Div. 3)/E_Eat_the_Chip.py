t = int(input())

for _ in range(t):
    h, w, xa, ya, xb, yb = map(int, input().split())

    if abs(xa - xb) < abs(ya - yb):
        print("Draw")
    else:
        if abs(xa - ya) % 2 != 0:
            print("Bob")
        else:
            print("Alice")
