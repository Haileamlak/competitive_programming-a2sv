
def translate(word):
    translated = ""
    for letter in word:
        if letter in 'AEIOUaeiou':
            translated += ' '
        else:
            translated += letter

    return translated

print(translate("books are my favorite resources to learn."))

try:
    1 / 3
except ZeroDivisionError as err:
    print(err)
except:
    print(True)
# else:
#     print("No error")
finally:
    print("Done")