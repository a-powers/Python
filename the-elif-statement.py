def positive_or_negative(number):
    if number > 0:
        return "Positive!"
    elif number < 0:
        return "Negative!"
    else:
        return "Neither! It's zero."

print(positive_or_negative(5))
print(positive_or_negative(-1))
print(positive_or_negative(0))



def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    elif operation == "power":
        return a**b
    else:
        return "I don't know what you want me to do!"

print(calculator("add", 3, 4))
print(calculator("subtract", 3, 4))
print(calculator("multiply", 3, 4))
print(calculator("divide", 3, 4))
print(calculator("power", 3, 4))


# #Coding Exercise 10: if statements
def even_or_odd(integer):
    if integer % 2 == 0:
        return "even"
    else:
        return "odd"
print(even_or_odd(3))


def truthy_or_falsy(booz):
    if bool(booz) == True:
        return "The value {0} is truthy".format(booz)
    else:
        return "The value {0} is falsy".format(booz)
print(truthy_or_falsy(0))

#Coding Exercise 11: if, else, and elif
def up_and_down(strings):
    return strings.swapcase()
print(up_and_down("HELLO"))


def negative_energy(abs_number):
    return abs(abs_number)
print(negative_energy(-9009))