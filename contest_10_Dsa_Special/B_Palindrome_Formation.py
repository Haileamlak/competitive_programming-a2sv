for _ in range(int(input())):
    n = int(input())
    word = input()
    dif = False
    same = False
    for i in range(n // 2):
        if word[i] == word[n - i - 1]:
            if dif:
                same = True
        
        else:
            if dif and same:
                print("No")
                break

            dif = True
    else:
        print("Yes")