guest = input()
host = input()
letters = input()

if sorted(guest + host) == sorted(letters):
    print("YES")
else:
    print("NO")