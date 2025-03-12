import random 
import math

def hello():
    print('Welcome to the Brain Games!\n')
    name=str(input('May I have your name?\n'))
    print('Hello', name,'!')
    print('Find the smallest common multiple of given numbers.\n')
    return name

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def lcm_three(a, b, c):
    return lcm(lcm(a, b), c)

def generate_unique_numbers(count=3, start=1, end=30):
    return random.sample(range(start, end + 1), count)

def game(name):
    while True:
        a, b, c = generate_unique_numbers()
        print(f'Question: {a}, {b}, {c}')
        correct = lcm_three(a,b,c)
        answer=input('Your answer:' )
        if answer.lower() == 'quit':  # Check for 'quit' before converting to int
            print(f'Goodbye, {name}! Thanks for playing!')
            break

        try:
            answer = int(answer)  # Convert to integer
            if answer == correct:
                print('Correct!\n')
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was {correct}.\n")
        except ValueError:  # Handle invalid input (non-integer or non-quit)
            print("Invalid input. Please enter a number or type 'quit' to exit.\n")

name = hello()
game(name)