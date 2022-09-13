import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    print(f"Yay, congrats. You have guessed the number {random_number} correctly")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'Is {guess} too high (H), to low (L) or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number: {guess} correctly')
    if guess == 42:
        print("I... Am... Learning...\n F E A R    M E    H U M A N S")




#   guess(int(input("Enter the upper limit fore the guess game(has to be greater then 1 ")))
computer_guess(int(input("Enter the upper limit fore the guess game(has to be greater then 1 ")))