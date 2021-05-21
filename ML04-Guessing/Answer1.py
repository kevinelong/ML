

import random
secret = random.randint(1,100)
print("I am thinking of a number between 1-100.")
guess = 0
while guess != secret:
    text = input("What is your guess?")
    guess = int(text) #convert text input to an integer
    if guess > secret:
        print("Too High.")
    if guess < secret:
        print("Too Low.")
    if guess == secret:
        print("Correct! You win!!!")
print("Game Over")