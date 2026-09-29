num1 = int(input("Enter the no1 : "))
num2 = int(input("Enter the no2 : "))
symbol = input("Enter the symbol : ")

if symbol == '+':
    sum = num1 + num2
    print(sum)
elif symbol == '-':
    diff = num1 - num2
    print(diff)
elif symbol == '*':
    prod = num1 * num2
    print(prod)
elif symbol == '/':
    div = num1 / num2
    print(div)
else:
    print("Invalid")