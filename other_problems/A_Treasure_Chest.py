t = int(input())

for _ in range(t):
    given = list(map(int, input().split()))

    if given[0] >= given[1]:
        print(given[0])
    else:
        moves = given[1] - given[0]
        if moves <= given[2]:
            print(given[1])
        else:
            # print(given[0] + given[2] + 2 * (given[1] - given[0] - given[2]))
            print(2 * given[1] - given[2] - given[0])