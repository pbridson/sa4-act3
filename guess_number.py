import random

number = random.randint(1, 20)

print("I'm thinking of a number between 1 and 20...")
count = 5
print(f"You can have {count} guesses.")
guess = int(input("What number am I thinking of? "))

while guess != number:
  try:
    count -= 1
    hint = ("low" if guess < number else "high")
    print (f"Sorry, your guess is too {hint}! You have {count} guesses left.")
    if count == 0:
      print(f"The number was {number}.")
      break
    guess = int(input("Try again or enter q to quit: "))
  except ValueError:
    print(f"You give up! The number was {number}.")
    break
else:   
  print("Congratulations! You guessed the right number.")
