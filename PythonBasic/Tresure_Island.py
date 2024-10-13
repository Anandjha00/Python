print('''
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
direction=input("you are at a cross road .where do you want to go ?\n\tType 'left' or 'right' : \n")
if direction=="left"or  direction=="Left":
    yourchoice=input(f"You have come to a lake. There is an island in the middle of the lake.\n\tType 'wait' to wait for a boat.Type 'swim'to swim across.\n")
    if yourchoice=="wait" or yourchoice== "Wait":
        doorcolor=input(f"There are three doors blue,green and yellow . Choose the color of door.\n\tType 'blue' ,'green'and 'yellow' for yellow door.")
        if doorcolor=="blue" or doorcolor=="Blue":
            print("There is a tiger in this room. You Lost!")
        elif doorcolor=="green" or doorcolor=="Green":
            print("This room is full of fire.You Lost!")
        elif doorcolor=="Yellow" or doorcolor=="yellow":
            print("You won the Game!")
        else:
            print("Invalid Input!")
    elif yourchoice=="Swim" or  yourchoice=="swim":
        print("A crocodile has eaten you.You lost the game!")
    else:
        print("Invalid Input !")
elif direction=="Right" or  direction=="right":
    print("You fall into a hole.You Lost!")
else:
    print("Invalid input !")
