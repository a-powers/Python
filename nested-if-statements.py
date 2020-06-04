ingredient1 = "Lasagna noodles"
ingredient2 = "Tomato sauce"

if ingredient1 == "Lasagna noodles":
    if ingredient2 == "Tomato sauce":
        print("I recommend making baked Lasagna.")
    else:
        print("Find an alternative to Tomato sauce before proceeding.")
else:
    print("I have no recommendations.")

# Second way

if ingredient1 == "Lasagna noodles" and ingredient2 == "Tomato sauce":
    print("I recommend making baked Lasagna.")
elif ingredient1 =="Lasagna noodles":
    print("Find an alternative to Tomato sauce before proceeding.")
else:
    print("I have no recommendations.")



# # Coding Exercise 12

# def divisible_by_three_and_four(a):
#     if a % 3 == 0 and a % 4 == 0:
#         return True
#     else:
#         return False
# print(divisible_by_three_and_four(12))



# def string_theory(a:str):
#     if (len(a) > 3) and a[0] == "S":
#         return True
#     else:
#         return False
# print(string_theory("Story"))