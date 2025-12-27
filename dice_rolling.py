from random import*
while True:
    choice = input("Roll the dice? (y or n): ").lower()

    if choice == "y":
        result = []
        number_of_dice = int(input("How many dice: "))
        for i in range(number_of_dice):
            result.append(randint(1, 6))
        print(result)
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
