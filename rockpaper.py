# #rock paper scissor game
import random
def rps():
    print("Welcome to Rock, Paper, Scissors game")
    choices = ['rock', 'paper', 'scissors']
    while True:
        ques = input("Do you want to play? (yes/no): ")
        if ques.lower() != "yes":
            print("Thank You!")
            break
        print("Let's play Rock, Paper, Scissors game!")
        choice = input("Enter 'rock' for Rock, 'paper' for Paper, or 'scissors' for Scissors: ").lower()
        print("Your Choice =", choice)
        computer_choice = random.choice(choices)
        print("Computer Choice =", computer_choice)

        if choice == computer_choice:
            print("It's a tie")
        elif (choice == 'rock' and computer_choice == 'scissors') \
                or (choice == 'paper' and computer_choice == 'rock') \
                or (choice == 'scissors' and computer_choice == 'paper'):
            print("You won!")
        else:
            print("You lost. Computer Wins!")

rps()




