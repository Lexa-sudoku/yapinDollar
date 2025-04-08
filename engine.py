def play_game(game_func, name):
    """Запуск игры с общей логикой."""
    print(f"\nHello, {name}!\n")

    rounds = 3

    for _ in range(rounds):
        question, correct_answer = game_func()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!\n")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!\n")
            return

    print(f"Congratulations, {name}!")
