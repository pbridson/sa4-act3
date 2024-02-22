number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))
while guess != number:
  try:
    hint = ("low" if guess < number else "high")
    guess = int(input(f"Sorry, your guess is too {hint}! Try again or enter q to quit: "))
  except:
    print(f"You give up! The number was {number}.")
    break
else:                 
  print("Congratulations! You guessed the right number.")
