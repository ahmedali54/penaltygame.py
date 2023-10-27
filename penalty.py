import random

# Define the goalkeeper's goal area
goalkeeper_position = [0, 1, 2]

def shoot_penalty():
    print("\nShoot to score a goal! Choose a position (0, 1, 2):")
    player_choice = input()

    if player_choice.isdigit() and int(player_choice) in goalkeeper_position:
        goalkeeper_choice = random.choice(goalkeeper_position)

        if player_choice == str(goalkeeper_choice):
            print("Saved by the goalkeeper! No goal.")
        else:
            print("GOAL! You scored!")

    else:
        print("Invalid position. Choose 0, 1, or 2.")

def main():
    print("Welcome to the Penalty Shootout Game!")

    while True:
        print("\nOptions:")
        print("1. Shoot a penalty")
        print("2. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            shoot_penalty()
        elif choice == '2':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
