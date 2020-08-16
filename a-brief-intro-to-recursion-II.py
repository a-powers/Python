# def reverse(str):
#     start_index = 0
#     last_index = len(str) -1
#     reversed_string = ""

#     while last_index >= start_index:
#         reversed_string += str[last_index]
#         last_index -= 1
    
#     return reversed_string
# print(reverse("straws"))




def reverse(str):
    if len(str) <=1:        #starting base case
        return str

    return str[-1] + reverse(str[:-1])

print(reverse("straw"))


# straw
# w + reverse(stra)
# w + a reverse(str)
# w + a + r reverse(st)
# w + a + r + t reverse(s)