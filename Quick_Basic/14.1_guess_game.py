#                   guess game
import random

number = random.randint(0, 10)

guess = int(input(
    "\nI'm thinkin about an number !! Can you guess that nubmer ? (in between 1 to 10) :: "))

while True:
    if(guess == number):
        break
    else:
        guess = int(input("\nNope. Try again ! "))
print("\nYou guessed it right ! i was thinking about ", number)
