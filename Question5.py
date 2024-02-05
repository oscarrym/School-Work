def calculation(num1,num2,operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    else:
        if num2 or num1 != 0:
            print("Error: Cannot divide by zero")
        else:
            result = num1 / num2
    return round(result, 2)

num1 = float(input("Enter first number: "))
operator = input("Input operator( +, -, *, / ): ")
num2 = float(input("Enter second number: "))
result = calculation(num1, num2, operator)

print({num1}, {operator}, {num2}, "=", {result})


