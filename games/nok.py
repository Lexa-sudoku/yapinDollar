import random
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def find_lcm_of_three_numbers(a, b, c):
    return lcm(lcm(a, b), c)

def generate_nok_question():
    numbers = [random.randint(1, 20) for _ in range(3)]
    correct_answer = find_lcm_of_three_numbers(*numbers)
    question = ' '.join(map(str, numbers))
    return question, correct_answer

def play_nok():
    return generate_nok_question()
