import random
def game():
    choices=["rock","paper","scissor"]
    user=input("enter the rock,paper,scissor")
    computer=random.choice(choices)
    print("user :"+user,"\ncomputer :"+computer)
    if user==computer:
        return game()
    elif user=="rock" and computer=="paper":
        print("winner is computer :",computer)
    elif user=="rock" and computer=="scissor":
        print("winner is user :",user)
    elif user=="paper" and computer=="scissor":
        print("winner is computer :",computer)
    elif user=="paper" and computer=="rock":
        print("winner is user :",user)
    elif user=="scissor" and computer=="rock":
        print("winner is computer :",computer)
    elif user=="scissor" and computer=="paper":
        print("winner is user :",user)
game()