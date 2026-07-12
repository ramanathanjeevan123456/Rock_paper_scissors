import random

def choices():
    user_choice = input("enter a choice(rock, paper, scissor): ")
    options = ["paper", "rock", "scissors"]
    computer_choice = random.choice(options)
    final = {"user" : user_choice, "pc" : computer_choice}
    return final
   
def check_win(user, pc):
    print(f"you chose {user} and computer chose {pc}")
    if user==pc:
        return "it's a tie!"
    elif user== "rock":
        if pc== "scissors":
         return "rock smashes scissors! you win!"
        else:
            return "you lost!"
    elif user== "paper":
        if pc== "rock":
         return "paper wraps rock! you win"
        else:
            return "you lost."
    elif user == "scissors":
        if pc=="paper":
         return "scissors cuts paper, you win!"
        else:
            return "you lost."
       
    elif user =="scissors" and pc=="rock":
        return "you lost"
    elif user =="paper" and pc=="scissors":
        return "you lost"
       
choices = choices()
result = check_win(choices["user"], choices["pc"])

print(result)
