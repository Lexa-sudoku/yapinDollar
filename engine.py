import random

def play_game(game_func):
    """Запуск игры с общей логикой."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!\n")

    # Общие параметры игры
    rounds = 3

    # Запуск раундов игры
    for _ in range(rounds):
        question, correct_answer = game_func()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        # Проверка правильности ответа
        if user_answer == str(correct_answer):
            print("Correct!\n")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!\n")
            return

    print(f"Congratulations, {name}!")
