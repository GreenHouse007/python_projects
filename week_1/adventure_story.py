print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

question_one = input("\nYou are on an island\n"
                     "Do you go left or right?\n").lower().strip()

if question_one == "left":
    question_two = input("\nThere is a river\n"
                         "Do you swim or wait?\n").lower().strip()
    if question_two == "wait":
        question_three = input("\nYou come to some ruins with 3 doors\n"
                               "What door do you choose? red, yellow, or blue?\n").lower().strip()
        if question_three == "red":
            print("\nYou are burned up by fire!\nGAME OVER.")
        elif question_three == "blue":
            print("\nYou are eaten by beasts!\nGAME OVER.")
        elif question_three == "yellow":
            print("\nYou find the treasure!\nYOU WIN.")
        else:
            print("GAME OVER.")
    else:
        print("\nYou are attacked by a trout.\nGAME OVER.")
else:
    print("\nYou fall into a hole.\nGAME OVER.")

