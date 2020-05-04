if 5 < 7 and "rain" == "rain":
    print("Both condition evaluate to True")


if 5 < 7 and "rain" == "fire":
    print("This will not print; one condition is False")


# shortcircuit evaluation -first condition was false; won't print

if "rain" == "fire" and 5 < 7:
    print("This will not print; one condition, the first, is False")




value = 95

if value > 90 and value < 100:
    print(value)

# shortcut

if 90 < value < 100:
    print(value)