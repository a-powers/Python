# Recursion is when a function calls itself.

# Not recusion; simple example

# def count_down_from(number):
#     start = number
#     while start > 0:
#         print(start)
#         start -= 1
# count_down_from(10)


# def count_down_from(number):
#     if number > 12:    # lines 14 and 15 are called base case; makes the recursion stop
#         return    # you may add an else: here but it's not needed, just a return
    
#     print(number)
#     count_down_from(number + 1)  #this is recusion

# count_down_from(1)


# def factorial(element):
#     if element == 1:
#         return element

#     return element * factorial(element - 1)
# print(factorial(5))

def elements(ints):
    if ints > 50:
        return ints

    return elements(ints + 1)
print(elements(48))