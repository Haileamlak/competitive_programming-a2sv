num1 = float(input("Enter a number: "))
operator = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print("Oops! Invalid operator. Please try again!")