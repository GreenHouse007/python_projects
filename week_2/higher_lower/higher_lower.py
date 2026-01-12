from art import logo, vs
from random import choice
from game_data import data


def ask_question(card_a, card_b):
    print(f"Compare A: {card_a['name']}")
    print(f"Description: {card_a['description']}")
    print(f"From: {card_a['country']}")
    print(vs)
    print(f"Against B: {card_b['name']}")
    print(f"Description: {card_b['description']}")
    print(f"From: {card_b['country']}\n")

    answer = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
    return answer


def is_correct(answer, card_a, card_b):
    a_followers = card_a["follower_count"]
    b_followers = card_b["follower_count"]

    if answer == "a":
        return a_followers > b_followers
    if answer == "b":
        return b_followers > a_followers

    return False


def game():
    print(logo)

    available_data = data.copy()
    if len(available_data) < 2:
        raise ValueError("Not enough data to play — need at least 2 items.")

    score = 0

    card_a = choice(available_data)
    available_data.remove(card_a)

    card_b = choice(available_data)
    available_data.remove(card_b)

    while True:
        answer = ask_question(card_a, card_b)

        if is_correct(answer, card_a, card_b):
            score += 1
            print(f"\nYou're right! Current score: {score}\n")

            if card_b["follower_count"] > card_a["follower_count"]:
                card_a = card_b

            if not available_data:
                print(f"\nYOU WIN! No items left. Final score: {score}")
                return score

            card_b = choice(available_data)
            available_data.remove(card_b)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return score


def main():
    while True:
        game()
        again = input("Do you want to play again? Type 'y' or 'n': ").strip().lower()
        if again != "y":
            break


main()
