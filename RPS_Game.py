import random

computer_input=['r','p','s']
computer_choice=random.choice(computer_input)
wins={
    'r':'s',
    'p':'r',
    's':'p'
}
while True:
    user_input=input("Enter your choice(R for Rock, P for Paper, S for Scissors) : ").lower()
    if user_input not in computer_input:
        print('Enter r, p, s in your choice!')
        continue
    if user_input==computer_choice:
        print("Draw")
        print("Please put another choice!")
    elif wins[computer_choice]==user_input:
        print('Computer won')
        print(f'Computer Choice {computer_choice} and user Choice {user_input}')
    else:
        print("user won")
        print(f'Computer Choice {computer_choice} and user Choice {user_input}')
        break
    
