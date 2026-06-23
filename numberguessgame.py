import random

# computer chooses random number
secret_number = random.randint(1, 100)
attempts=0
print("=== Number Guessing Game ===")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    attempts+=1
    if guess > secret_number:
        print("Too High! Try again.")

    elif guess < secret_number:
        print("Too Low! Try again.")

    else:
        print("Congratulations! You guessed the number.")
        print("attempts taken :",attempts )
        break