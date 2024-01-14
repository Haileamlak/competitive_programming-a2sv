t = int(input())

for _ in range(t):
    n = int(input())
    mes = input()

    i = 0
    while i < len(mes):
        temp = mes[i]
        i += 1
        while mes[i] != temp:
            i += 1
        
        print(temp,end="")
        i += 1
    print()
