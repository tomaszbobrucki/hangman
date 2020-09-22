# Write your code here
import random
import string

print("H A N G M A N")
while True:
    choice = input('Type "play" to play the game, "exit" to quit:')
    if choice == "play":
        words = ["python", "java", "kotlin", "javascript"]
        word = random.choice(words)
        attempts = 8
        guess = "-" * len(word)
        tries = []

        while attempts > 0:
            print()
            print(guess)
            if guess == word:
                print("You guessed the word!")
                print("You survived!")
                print()
                break

            letter = input("Input a letter:")
            if len(letter) != 1:
                print("You should input a single letter")
            elif letter not in string.ascii_lowercase:
                # print("Please enter a lowercase English letter")
                print("It is not an ASCII lowercase letter")
            elif letter in guess:
                # attempts -= 1
                # print("You've already guessed this letter")
                print("You already typed this letter")
            elif letter in tries:
                # print("You've already guessed this letter")
                print("You already typed this letter")
            elif word.find(letter) != -1:
                num = 0
                for _ in range(word.count(letter)):
                    index = word.find(letter, num)
                    guess = guess[:index] + letter + guess[index + 1:]
                    num = index + 1
            else:
                attempts -= 1
                # print("That letter doesn't appear in the word")
                print("No such letter in the word")
                tries.append(letter)

            if attempts == 0:
                print("You lost!")
                print()
                break
    elif choice == "exit":
        break
    else:
        continue

# print("Thanks for playing!")
# print("We'll see how well you did in the next stage")
# + word[:3] + "-" * (len(word) - 3) + ":")
# if guess == word:
# print("You survived!")
# else:
# print("You lost!")
