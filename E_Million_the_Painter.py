
def the_char(ch1, ch2):
    if ch1 == 'M' and ch2 == 'Y':
        return 'C'
    if ch1 == 'M' and ch2 == 'C':
        return 'Y'
    return 'M'

n = int(input())
poss = False
canvas = input()
paintable = "Yes"
checked = False
ch = ""

if canvas[0] == '?':
    checked = True
for i in range(1, len(canvas)):
    if canvas[i].isalpha():
        if canvas[i] == canvas[i - 1]:
            paintable = "No"
            break

    elif not checked:
        if i < len(canvas) - 1:
            if canvas[i - 1].isalpha() and canvas[i + 1].isalpha():
                if canvas[i - 1] != canvas[i + 1]:
                    paintable = "No"
                else:
                    paintable = "Yes"
                    checked = True
            else:
                paintable = "Yes"
                checked = True
        else:
            paintable = "Yes"
            checked = True
if not checked and paintable == "Yes":
    paintable = "No"
print(paintable)




# if canvas[i].isalpha() and canvas[i - 1].isalpha() and canvas[i] == canvas[i - 1]:
#     paintable = "No"