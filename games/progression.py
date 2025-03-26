import random

def generate_progression():
    """Генерация прогрессии и возвращение вопроса с пропущенным элементом."""
    start = random.randint(1, 5)
    ratio = random.randint(2, 5)  # Порядок прогрессии
    progression = [start * ratio**i for i in range(10)]  # Прогрессия из 10 чисел

    hidden_index = random.randint(0, 9)  # Скрытый элемент в случайной позиции
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'  # Скрытие числа

    question = ' '.join(map(str, progression))  # Преобразуем прогрессию в строку

    return question, correct_answer

def play_progression():
    """Функция для игры 'Геометрическая прогрессия'."""
    return generate_progression()
