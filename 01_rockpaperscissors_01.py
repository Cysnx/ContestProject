import random
score=0
choices = {1: 'Rock', 2: 'Paper', 3: 'Scissor'}
def rock_paper_scissor(user_input,machine_input,score):
    ans=[choices[user_input],choices[machine_input]]
    if ans==['Rock', 'Scissor'] or ans==['Paper', 'Rock'] or ans==['Scissor', 'Paper']:
        score+=1
        result='You Win!'
    else:
        result='You Lose!'
    return result, score
for i in range(5):
    user_input = int(input("Enter your choice: 1: Rock, 2: Paper, 3: Scissor "))
    if user_input == 1 or user_input == 2 or user_input == 3:
        machine_input = random.randint(1, 3)
        if user_input == machine_input:
            print(f"Both sides: {choices[user_input]}. It is a tie!")
        else:
            print(f"You: {choices[user_input]}, Opponent: {choices[machine_input]}")
            result, score=rock_paper_scissor(user_input,machine_input,score)
            print(result)
    else:
        print("Invalid choice.")
print(f"Thank you for playing! Your score is: {score}")