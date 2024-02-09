import collections
n = int(input())

res = collections.Counter(input())

if res['A'] > res['D']:
    print("Anton")

elif res['D'] > res['A']:
    print("Danik")

else:
    print("Friendship")