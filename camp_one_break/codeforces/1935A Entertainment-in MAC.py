for _ in range(int(input())):
    n = int(input())
    word = input()

    rev = False
    for i in range(len(word) // 2):
        if word[i] > word[-1 - i]:
            rev = True
            break
        elif word[i] < word[-1 -i]:
            break

    if rev:
        word = ''.join(reversed(list(word)))
        n -= 1
       
    n %= 2 
    if n:
        print(word + ''.join(reversed(list(word))))
    else:
        print(word)
    # else:
    #     if n:
