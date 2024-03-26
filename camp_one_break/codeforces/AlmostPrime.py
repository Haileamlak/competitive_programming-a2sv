m = int(input())

def almost_primes(n):
    temp = set()

    d = 2
    while d * d <= n:
        while n % d == 0:
            temp.add(d)
        
            n //= d
        d += 1

    if n > 1:
        temp.add(n)
    
    return 1 if len(temp) == 2 else 0

res = 0
for num in range(2, m + 1):
    res += almost_primes(num)

print(res)
