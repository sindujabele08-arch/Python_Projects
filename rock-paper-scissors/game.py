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
game_images= [rock,paper,scissors]
user_choice=int(input("what is your choice ? type 0 for rock,type 1 for paper,type 2 for scissors ")) 
user_choice >=0 and user_choice<=2
print(game_images[user_choice])


computer_choice = random.randint(0,2)
print(computer_choice)
print(game_images[computer_choice])

if user_choice>2 or user_choice<0:
    print("you entered invalid number.you loose.")

elif user_choice==0 and computer_choice==2:
    print("you win")
elif computer_choice==0 and user_choice==2:
    print("you loose.")
elif user_choice> computer_choice:
    print("you win")
elif computer_choice> user_choice:
    print("you loose.")
elif computer_choice==user_choice:
    print("its a draw")
