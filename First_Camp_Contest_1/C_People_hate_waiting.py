n = int(input())
people = list(map(int, input().split()))

people.sort()
res = 0
wait = 0

for person in people:
    if person >= wait:
        res += 1
        wait += person


print(res)