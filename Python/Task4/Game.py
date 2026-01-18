import random

print("Welcome to Rock Paper Scissors Game")
print("Choose your option:")
print("1: Rock")
print("2: Paper")
print("3: Scissors")

user_score = 0
computer_score = 0

while True:
    user_input = input("\nEnter 1, 2, or 3: ")

    if user_input not in ["1", "2", "3"]:
        print("Invalid input. Try again.")
        continue

    user_choice = int(user_input)
    computer_choice = random.randint(1, 3)

    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    print("You chose:", choices[user_choice])
    print("Computer chose:", choices[computer_choice])

    if user_choice == computer_choice:
        print("Result: It's a tie")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("Result: You win")
        user_score += 1
    else:
        print("Result: You lose")
        computer_score += 1

    print("Score: You:", user_score, "| Computer:", computer_score)

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != "y":
        print("\nThanks for playing!")
        break
