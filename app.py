import random


def guessNum():
    print('''I am thinking of a number between 1 and 10.
Take a guess. You have six chances to guess.''')
    number = random.randint(1, 10)
    count = 1
    guess = int(input())
    while guess != number and count < 5:
        count = count + 1
        if guess < number:
            print('Your guess is too low. Take a guess again')
            guess = int(input())
        elif guess > number:
            print('Your guess is too high. Take a guess again')
            guess = int(input())
    if guess == number:
        print('Good job! You guessed my number in ' + str(count) + ' guesses!')
    else:
        print("Sorry")


guessNum()
