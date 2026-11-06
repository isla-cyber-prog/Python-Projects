import random

choices = ["rock", "paper", "scissors"]

while True:

    computer = random.choice(choices)

    player = input("Choose rock, paper, or scissors: ").lower()

    if player not in choices:
        print("Invalid choice!")
        continue

    print(f"\nYou chose {player}")
    print(f"Computer chose {computer}")

    if player == computer:
        print("It's a tie!")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("You win!")

    else:
        print("Computer wins!")

    again = input("\nPlay again? (y/n): ")

    if again.lower() != "y":
        break

print("Thanks for playing!")
