t = int(input())

for _ in range(t):
    yes = input()
    
    if yes[0] == 'Y':
        char = ['Y', 'e', 's']
    
    elif yes[0] == 'e':
        char = ['e', 's', 'Y']

    elif yes[0] == 's':
        char = [ 's', 'Y', 'e']
    else:
        char = [ 's', 'Y', 'e']
    

    res = "YES"
    j = 0
    for i in range(len(yes)):
        if yes[i] != char[j % 3]:
            res = "NO"
            break

        j += 1

    print(res)