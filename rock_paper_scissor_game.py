from random import*

res = (1, 2, -3)
name = {"r": "🪨", "p": "📄", "s": "✂️"}
choices = tuple(name.keys())

def get_your_choice():
    while True:
        your_choice = input("Rock, Paper, Scissors? type (r / p / s) or type 'q' to quit: ").lower()
        if your_choice in choices or your_choice == 'q':
            return your_choice
        else :
            print("Invalid choice!")    

def determine_winner(your_choice, computer_choice):
    print(f"Computer chose: {name[computer_choice]}  VS  Your choice: {name[your_choice]}")
    result = ord(computer_choice) - ord(your_choice)
    if result == 0:
        return "TIE!"
    elif result in res:
        return "YOU WON!"
    else:
        return "YOU LOST!"

def start_game():
    while True:

        your_choice = get_your_choice()
        if your_choice == 'q':
            print("Thanks for playing!")
            break
        computer_choice = choice(choices)

        print(determine_winner(your_choice, computer_choice))

start_game()


