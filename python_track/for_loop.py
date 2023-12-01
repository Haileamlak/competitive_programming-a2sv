for i in range(5):
    if i % 2 == 0:
        print(str(i) + " is even.")
    else:
        print(str(i) + " is odd.")

def power(base, pow):
    res = 1
    for i in range(pow):
        res *= base
    
    return res

print(power(3, 4))