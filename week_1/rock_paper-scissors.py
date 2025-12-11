import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to rock paper scissors")
player = int(input("\nPlease pick rock, paper, or scissors to play\n"
               "Type: 0 for rock, 1 for paper, 2 for scissors:\n").strip())

number = random.randint(0, 2)

images = [rock, paper, scissors]

print("\nYou choose:\n" + images[player])
print("I choose:\n" + images[number])

if player == number:
    print("It's a tie!")
elif player == 0 and number == 1:
    print("I win!")
elif player == 0 and number == 2:
    print("You win!")
elif player == 1 and number == 2:
    print("I win!")
elif player == 1 and number == 0:
    print("You win!")
elif player == 2 and number == 0:
    print("I win!")
elif player == 2 and number == 1:
    print("You win!")
else:
    print("\nNot a valid entry. Try again.")
