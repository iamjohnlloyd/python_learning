import random

random_number = random.randint(1, 10)  # numbers 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

continue_playing = 'yes'

while continue_playing == 'yes':

    user_guess = int(input("Guess a number between 1 and 10: "))
    print(random_number)

    if user_guess < random_number:
        print("Too low, try again!")
        random_number = random.randint(1, 10)
    elif user_guess > random_number:
        print("Too high, try again!")
        random_number = random.randint(1, 10)
    else:
        print("You guessed it! You won!")
        random_number = random.randint(1, 10)
        question = input("Would you like to continue playing? ")
        if question != 'yes':
            continue_playing = 'no'
            break
