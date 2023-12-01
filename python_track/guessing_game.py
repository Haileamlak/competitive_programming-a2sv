secret = "ethiopia"
guess = ""

win = False
tries = 3
while tries > 0 and not win:
    guess = input("Enter your guess: ")
    if guess == secret:
        win = True
    tries -= 1

if tries == 0:
    print("You loss!")
else:
    print("You win!")