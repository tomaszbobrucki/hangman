def what_to_do(instructions):
    phrase = "Simon says"
    if instructions.startswith(phrase):
        return "I " + instructions[11:]
    elif instructions.endswith(phrase):
        number = instructions.find(phrase)
        return "I " + instructions[:number - 1]
    else:
        return "I won't do it!"
# what_to_do(input())
