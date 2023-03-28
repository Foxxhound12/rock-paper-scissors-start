import random
#import random          (wenn es vorher noch nicht importiert wurde)
#RockPaperScissors
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

#Write your code below this line 👇



hands = [rock, paper, scissors]


player = int(input("Welcome to rock, paper, scissors! Please make your choice: 0=rock, 1=paper, 2=scissors\n"))
if 0 <= player <= 2:
    print(hands[player])

print("Now it is the turn of your enemy:")
enemy = random.randint(0,2)
print(f"The computer chose {enemy}\n{hands[enemy]}")

if player == enemy:
    print("It's a tie!")
elif player == 0 and enemy == 2:
    print("You win!")
elif player == 1 and enemy == 0:
    print("You win!")
elif player == 2 and enemy == 1:
    print("You win!")
elif player < 0 or player > 2:
    print("You typed in an invalid number! You lose!")
else:
    print("You lose!")