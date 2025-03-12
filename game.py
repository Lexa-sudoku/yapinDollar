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


def game(name):
    while True:
        a=random.randint(1, 30)
        b=random.randint(1, 30)
        c=random.randint(1, 30)
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