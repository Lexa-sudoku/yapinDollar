import random

def generate_progression():
    start = random.randint(1, 5)
    ratio = random.randint(2, 5)
    progression = [start * ratio**i for i in range(10)]

    hidden_index = random.randint(0, 9)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'

    question = ' '.join(map(str, progression))
    return question, correct_answer

def play_progression():
    return generate_progression()
