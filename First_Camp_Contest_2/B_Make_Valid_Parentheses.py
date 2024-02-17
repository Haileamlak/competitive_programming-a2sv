bracket = input()

open = 0
closed = 0

res = len(bracket)

for x in bracket:
    if x == '(':
        open += 1
    elif x == ')':
        if open:
            open -= 1
        else:
            closed += 1
    

res -= open
res -= closed
print(res)