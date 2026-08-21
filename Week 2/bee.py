WORDS = {"PAIR":4, "HAIR": 4, "CHAIR":5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")
    for word, points in WORDS.items():
        print(f"{word} was worth {points} points.")
    # print("your letters are: A I P C H R G")

    # while len(WORDS) > 0:
    #     print(f"{len(WORDS)} words left!")
    #     guess = input("Guess the word: ")

    #     if guess == "GRAPHIC":
    #         WORDS.clear()
    #         print("You've won the game!")
    #     if guess in WORDS.keys():
    #         points = WORDS.pop(guess)
    #         print(f"Good job! You scored {points} points.")

    # print("That's the game!")


main()
