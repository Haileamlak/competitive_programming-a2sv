num = 5

if num % 2 == 0:
    print(f"{num} is an even number!")
else:
    print(f"{num} is an odd number!")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def are_equal(num1, num2):
    if num1 == num2:
        return True
    else:
        return False
nm = max_num(1,2,3)
print(nm)