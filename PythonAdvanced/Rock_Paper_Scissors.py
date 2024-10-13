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
list =[rock,paper,scissors]

your_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if your_choice==-0:
    print("invalid input! You Lost !")
elif your_choice==0:
    print(rock)
elif your_choice==1:
    print(paper)
elif your_choice==2:
    print(scissors)
else:
    print("invalid input!")

computer_choice=random.choice(list)
if  your_choice<=2 and your_choice!=0:
    print(f"Computer Choice{computer_choice}")




if your_choice==0 and computer_choice==list[0]:
    print("Match Draw!")
elif your_choice==1 and computer_choice==list[1]:
    print("Match Draw!")
elif your_choice==2 and computer_choice==list[2]:
    print("Match Draw !")


elif your_choice==0 and computer_choice==list[1]:
    print("You Lost !")
elif your_choice==1 and computer_choice==list[0]:
    print("You Win !")

elif your_choice==0 and computer_choice==list[2]:
    print("You Win!")
elif your_choice==2 and computer_choice==list[0]:
    print("You Lost!")

elif your_choice==1 and computer_choice==list[2]:
    print("You Lost!")
elif your_choice==2 and computer_choice==list[1]:
    print("You Win !")
