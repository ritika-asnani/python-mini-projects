import  random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]
names = ["Rock", "Paper", "Scissors"]

while True:
    try:
        mode = int(input("\nChoose game mode\n"
                            "1 -> Best of 3\n"
                            "2 -> Best of 5\n"
                            "Your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if mode == 1:
        wins_needed = 2
        break
    elif mode == 2:
        wins_needed = 3
        break
    else:
        print("Invalid choice. Try again.")

user_score = 0
computer_score = 0
round_no = 1

while user_score < wins_needed and computer_score < wins_needed:

    print(f"\n-- Round {round_no} --")
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    try:
        user_choice = int(input("\nChoose your move\n"
                                "0 -> Rock\n"
                                "1 -> Paper\n"
                                "2 -> Scissors\n"
                                "9 -> Exit\n"
                                "Your choice: "
        ))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if user_choice == 9:
        print("\nThanks for playing!")
        break

    if user_choice > 2 or user_choice < 0:
        print("Invalid input. Try again.")
        continue

    computer_choice = random.randint(0, 2)

    print(f"\nYou chose {names[user_choice]}")
    print(choices[user_choice])

    print(f"Computer chose {names[computer_choice]}")
    print(choices[computer_choice])

    if computer_choice == user_choice:
        print("Draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
        (user_choice == 1 and computer_choice == 0) or \
        (user_choice == 2 and computer_choice == 1):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    round_no += 1

print("\n------------------------")
if user_score == wins_needed:
    print("YOU WON THE GAME!")
else:
    print("COMPUTER WON THE GAME!")

print(f"\nFinal Score -> You: {user_score} | Computer: {computer_score}")
print("------------------------")