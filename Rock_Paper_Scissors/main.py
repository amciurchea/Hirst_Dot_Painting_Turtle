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

# Write your code below this line 👇


choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. '))
computer = random.randint(0, 3)

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

if choice == 0 and computer == 1:
    print("You lose!")
elif choice == 0 and computer == 2:
    print("you win!")
elif choice == 1 and computer == 0:
    print("You win!")
elif choice == 1 and computer == 2:
    print("You lose!")
elif choice == 2 and computer == 0:
    print("You win!")
elif choice == 2 and computer == 1:
    print("You win!")
else:
    print("Nobody wins!")
