from random import randint

attempts = 0
guess = 0
secret_number = randint(1, 100)
name = input("What's your name? ")

print(f"Alright {name}, I have thought of a number between 1 and 100.\nYou have 8 attempts to guess it.")

while attempts < 8:
    guess = int(input("What's your guess? "))
    attempts += 1

    if guess < secret_number:
        print("My number is higher.")
    elif guess > secret_number:
        print("My number is lower.")
    else:
        print(f"Congratulations {name}! You guessed it in {attempts} attempts.")
        break

if guess != secret_number:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
