# Recursion is when a function calls itself.

# Not recusion; simple example

# def count_down_from(number):
#     start = number
#     while start > 0:
#         print(start)
#         start -= 1
# count_down_from(5)


def count_down_from(number):
    if number <= 0:    # lines 14 and 15 are called base case; makes the recursion stop
        return
    # you may add an else: here but it's not needed
    print(number)
    count_down_from(number - 1)  #this is recusion

count_down_from(10)