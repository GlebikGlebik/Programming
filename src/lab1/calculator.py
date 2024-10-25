import math

print("Please enter two numbers you want to calculate by line")
n1, n2 = [int(input()) for _ in "ab"]
print("Enter a sign of operation you want to execute")
o1 = input()

def calculator(number_1, number_2, operation):
    "Функция считывает знак операции, которую нужно выполнить и выполняет ее"

    operations = {
        "+": number_1 + number_2,
        "-": number_1 - number_2,
        "*": number_1 * number_2,
        "/": number_1 / number_2,
        "//": number_1 // number_2,
        "^": pow(number_1, number_2),
        "√": pow(number_2, pow(number_1, -1)),
        "log": math.log(number_1, number_2),
    }
    return operations[operation]

print(calculator(n1, n2, o1))
