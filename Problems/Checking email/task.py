def check_email(string):
    if " " in string:
        return False
    if "@" not in string:
        return False
    number = string.find("@")
    if string.find(".", number) == -1:
        return False
    if string[number + 1] == ".":
        return False
    return True

# print(check_email("good.email@example.com"))
