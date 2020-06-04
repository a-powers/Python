zip_code = "90210"

# check

if len(zip_code) == 5:
    check = "Valid"
else:
    check = "Invalid"
print(check)


# alternate way; must only contain one "if" and one "else"
new_zip_code = "48084"

check = "Valid" if len(new_zip_code) == 5 else "Invalid"
print(check)

newest = "Yes" if len(new_zip_code) == 5 else "No"
print(newest)


def updated_license(some_string):
    if len(new_zip_code) == 5:
        return f"yes, {some_string} has been updated"
    else:
        "no, expired"
print(updated_license("45345"))