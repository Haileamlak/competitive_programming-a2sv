t = int(input())

for _ in range(t):
    r = int(input())

    if r >= 1900:
        print("Division 1")
    elif r >= 1600 and r <= 1899:
        print("Division 2")
    elif r <= 1399:
        print("Division 4")
    else:
        print("Division 3")