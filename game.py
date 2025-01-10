import random
import sys

print("Hello! Let's play a game!")
print("I have a number in my mind 1 to 100. Can you guess it?")

number = random.randint(1, 100)
guess = 0


while True:
 try:
    guess = input("Your guess: ")
    if guess.lower() == "exit":
        print("Goodbye!")
        sys.exit()
    guess = int(guess) 
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("Congratulations! You guessed the number.")
        break
 except ValueError:
    print("Invalid input. Please enter a number.")


