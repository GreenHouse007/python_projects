from art import logo
from random import randint

EASY_TURNS = 10
HARD_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")
        return turns

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
    if difficulty == "easy":
        return EASY_TURNS
    elif difficulty == "hard":
        return HARD_TURNS
    else:
        print("Invalid choice, defaulting to 'easy'.")
        return EASY_TURNS

def game_loop():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    turns = set_difficulty()
    answer = randint(1, 100)

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


def main():
    while True:
        game_loop()
        again = input("Do you want to play again? Type 'y' or 'n': ").strip().lower()
        if again != "y":
            break


main()