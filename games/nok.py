import random
import math

def lcm(a, b):
    """Вычисление НОК для двух чисел."""
    return abs(a * b) // math.gcd(a, b)

def find_lcm_of_three_numbers(a, b, c):
    """Вычисление НОК для трёх чисел."""
    return lcm(lcm(a, b), c)

def generate_nok_question():
    """Генерация вопроса для игры 'НОК'."""
    numbers = [random.randint(1, 20) for _ in range(3)]  # Генерация трех случайных чисел
    correct_answer = find_lcm_of_three_numbers(*numbers)
    question = ' '.join(map(str, numbers))
    return question, correct_answer

def play_nok():
    """Функция для игры 'НОК'."""
    return generate_nok_question()
