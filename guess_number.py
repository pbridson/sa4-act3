number = 10

print("I'm thinking of a number...")
count = 5
print(f"You can have {count} guesses.")
guess = int(input("What number am I thinking of? "))

while guess != number:
  try:
    count -= 1
    print (f"Sorry, that's not it! You have {count} guesses left.")
    if count == 0:
      print(f"The number was {number}.")
      break
    guess = int(input("Try again or enter q to quit: "))
  except:
    print(f"You give up! The number was {number}.")
    break
else:                 
  print("Congratulations! You guessed the right number.")
