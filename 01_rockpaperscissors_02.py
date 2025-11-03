import random
score=0
WINNERS = {(1,3): "You win! Rock breaks scissors!",
           (3,2): "You win! Scissors cut paper!",
           (2,1): "You win! Paper covers rock!"
           }
LOSERS = {(1,2): "You lose! Paper covers rock!",
          (2,3): "You lose! Scissors cut paper!",
          (3,1): "You win! Rock breaks scissors!",}

for i in range(5):
    computer_input = random.randint(1, 3)
    user_choice = int(input("Enter your choice: 1: Rock, 2: Paper, 3: Scissor "))
    while user_choice not in [1,2,3]:
        print("Invalid choice. Please try again.")
        user_choice = int(input("Enter your choice: 1: Rock, 2: Paper, 3: Scissor "))
    if computer_input == user_choice:
        print("It's a draw!")
    elif (user_choice,computer_input) in WINNERS:
        score+=1
        print(WINNERS[user_choice,computer_input])
    else:
        print(LOSERS[user_choice, computer_input])
print(f"You won {score} round(s).")