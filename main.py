from random_word import RandomWords as rw
import time

# Greeting
print(
    """
      Welcome to WORLD of WORD!!!

      ONLY 1% people can solve this game.
      Try your luck darling.
      """
)

# Initialising the module and returning a single random word
def generate_word():
    r = rw()
    return r.get_random_word()

while True:
    computer_generate = generate_word()
    print("A new word has been generated. Try to guess it!")  # This line might need to be removed or commented out to keep the word secret
    # Uncomment the next line if you want to see the word for testing purposes
    print(computer_generate)
    time.sleep(5)  # Wait for 5 seconds before allowing the user to guess

    attempts = 0
    while True:
        # User Input
        user_choice = input("Choose a word to play game or type 'q' to quit: ")

        if user_choice.lower() == "q":
            print("Thank you for playing!")
            break

        print(f"Your guessed word is: {user_choice}")

        # Main game logic
        attempts += 1
        if computer_generate == user_choice:
            print("Congrats! You guessed the word!")
            print(f"It took you {attempts} attempts.")
            break
        else:
            print("Oops, you guessed the word wrong. Try again!")

    if user_choice.lower() == "q":
        break
