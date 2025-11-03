import random
score=0
for i in range(5):
    user_input = int(input("Enter your choice: 1: Rock, 2: Paper, 3: Scissor "))
    if user_input == 1:
        ans = random.randint(1, 3)
        if ans == 1:
            print("Rock. Tie!")
            score=score
        elif ans == 2:
            print("Paper. You Lost!")
            score=score
        elif ans == 3:
            print("Scissor. You Win!")
            score=score+1
    elif user_input == 2:
        ans = random.randint(1, 3)
        if ans == 1:
            print("Rock. You Win!")
            score=score+1
        elif ans == 2:
            print("Paper. Tie!")
            score=score
        elif ans == 3:
            print("Scissor. You Lost!")
            score=score
    elif user_input == 3:
        ans = random.randint(1, 3)
        if ans == 1:
            print("Rock. You Lost!")
            score=score
        elif ans == 2:
            print("Paper. You Win!")
            score=score+1
        elif ans == 3:
            print("Scissor. Tie!")
            score=score
    else:
        print("Please enter a valid choice.")
print(f"You won",score, "times.")