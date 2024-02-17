for _ in range(int(input())):
    n, m = map(int, input().split())
    petya = list(map(int, input().split()))
    vasya = list(map(int, input().split()))

    pl = 0
    pr = n - 1
    vl = 0
    vr = m - 1

    res = 0

    for i in range(n):
        pet1 = max(abs(petya[pl] - vasya[vl]), abs(petya[pl] - vasya[vr]))
        pet2 = max(abs(petya[pr] - vasya[vl]), abs(petya[pr] - vasya[vr]))
        if pet1 > pet2:
            res += pet1
            if abs(petya[pl] - vasya[vl]) > abs(petya[pl] - vasya[vr]):
                vl += 1
            else:
                vr -= 1
        else:
            res += pet2
            if abs(petya[pr] - vasya[vl]) > abs(petya[pr] - vasya[vr]):
                vl += 1
            else:
                vr -= 1
    
    print(res)

    