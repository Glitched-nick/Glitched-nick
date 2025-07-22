import random

user_score = 0
comp_score = 0
options = ["rock", "paper", "scissors"]

while True:
    user = input("Choose rock, paper, or scissors: ").lower()
    if user not in options:
        print("Invalid choice.")
        continue

    comp = random.choice(options)
    print("You:", user)
    print("Computer:", comp)

    if user == comp:
        print("Tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        comp_score += 1

    print("Score: You", user_score, "-", comp_score, "Computer")

    again = input("Play again? (y/n): ").lower()
    if again != "y":
        break
