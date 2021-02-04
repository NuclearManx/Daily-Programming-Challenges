def twenty_four(num1, num2, num3, num4, op1, op2, op3):
    if op3(op2(op1(num1, num2), num3), num4) == 24:
        return True
    if op3(op1(num1, op2(num2, num3)), num4) == 24:
        return True
    if op1(num1, op2(num2, op3(num3, num4))) == 24:
        return True

    return False

def twenty_four_player(num1, num2, num3, num4):
    operators = [add, subtract, multiply, divide]

    for op1 in operators:
        for op2 in operators:
            for op3 in operators:
                if twenty_four(num1, num2, num3, num4, op1, op2, op3):
                    return True

    return False

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 99999
    return a / b


print(twenty_four_player(2, 2, 2, 3))