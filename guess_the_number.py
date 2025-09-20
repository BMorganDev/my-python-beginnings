import random

# Guess the Number Game
print("Welcome to the Guess the Number Game!")
print("I am thinking of a number between 1 and 20.")

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)
guess = None
attempts = 0

# Loop until the user guesses correctly
while guess != secret_number:
    guess = int(input("Take a guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")

print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
