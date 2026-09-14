import random

print("================================")
print("     NUMBER GUESSING GAME")
print("================================")

number = random.randint(1, 100)
attempts = 0

print("I have selected a number between 1 and 100.")
print("Try to guess it!")

while True:
try:
guess = int(input("Enter your guess: "))
attempts += 1

if guess < number:
print("Too Low! Try again.")
elif guess > number:
print("Too High! Try again.")
else:
print("Congratulations! You guessed the correct number.")
print("Number of attempts:", attempts)
break

except ValueError:
print("Please enter a valid number.")