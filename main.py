from engine import play_game
from games.progression import play_progression
from games.nok import play_nok

def main():
    # Приветствие и выбор игры
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!\n")

    print("Choose a game:")
    print("1. Geometric Progression")
    print("2. Smallest Common Multiple (LCM)")
    print("0. Exit")

    while True:
        choice = input("Please enter the number of the game you want to play: ")

        if choice == "1":
            print("\nStarting the Geometric Progression game...")
            play_game(play_progression)
        elif choice == "2":
            print("\nStarting the Smallest Common Multiple (LCM) game...")
            play_game(play_nok)
        elif choice == "0":
            print("Goodbye! See you next time!")
            break
        else:
            print("Invalid choice! Please enter a valid number (1, 2, or 0).")

if __name__ == '__main__':
    main()
