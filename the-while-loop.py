# the while loop - runs as long as code is True

# count = 0

# while count <= 5:
#     print(count)
#     count +=1



# invalid_number = True

# while invalid_number:
#     user_value = int(input("Please enter a number greater than 10: "))
#     if user_value > 10:
#         print(f"Thanks, that works! {user_value} is a great choice.")
#         invalid_number = False
#     else:
#         print("That doesn't work.  Try again.")



def fizzbuzz(numberz):
    numbers = 1

    while numbers < numberz:
        if numbers % 3 == 0 and numbers % 5 == 0:
            print("FizzBuzz")
        elif numbers % 3 == 0:
            print("Fizz")
        elif numbers % 5 == 0:
            print("Buzz")
        else:
            print(numbers)
        numbers += 1
fizzbuzz(300)