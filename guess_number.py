number = "10"

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")
while guess != number:
  guess = input("Sorry! Try again or enter q to quit: ")
  if guess == "q":
    print(f"You give up! The number was {number}.")
    break
else:                 
  print("Congratulations! You guessed the right number.")
