def get_guess():
    # guess = 10
    # guess = input("Enter a guess: ")
    guess = int(input("Enter a guess: "))
    return guess

# print(get_guess())

def main():
    guess = get_guess()
    if guess == 30:
        print("Correct!")
    else:
        print("Incorrect!")
    print(guess)

main()