#EXTRA
import random
secret = random.randint(1,100)
print("I am thinking of a number between 1-100.")
guess = 0
playing = True
while playing:
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
    play_again = input("Press 'Enter' to play again or type 'quit' to quit.")
    if play_again == 'quit':
        playing = False
    else:
        guess = 0
        secret = random.randint(1,100)
print("Thanks for playing!")