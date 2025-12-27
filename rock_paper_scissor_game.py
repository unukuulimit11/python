import random as r
choices = ("r", "p", "s")
name = {"r": "🪨", "p": "📄", "s": "✂️"}
while True:
    your_choice = input("Rock, Paper, Scissor? type (r / p / s) or type 'q' to quit: ").lower()

    if your_choice == "q":
        print("Thank you for playing😇")
        break
    if your_choice not in choices:
        print("Invalid choice!")
        continue
    computer_choice = r.choice(choices)
    print(f"Computer chose: {name[computer_choice]}  VS  Your choice: {name[your_choice]}")
    result = ord(computer_choice) - ord(your_choice)
    if result == 0:
        print("IT IS A TIE")
    elif result == 1 or result == 2 or result == -3:
        print("YOU WON!")
    else:
        print("YOU LOST!")

