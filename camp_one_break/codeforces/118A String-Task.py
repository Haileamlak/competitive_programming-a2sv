word = input()

temp = set('AaEeIiOoUuYy')
res = []
for letter in word:
    if letter not in temp:
        res.append('.' + letter.lower())

print(''.join(res))