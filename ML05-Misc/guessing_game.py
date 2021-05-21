# There are two players in the game. One is the guesser and the other is the secret holder.
# first the secret holder picks a number
# second the guesser guesses
# third the secret holder provides feedback
# guess again until we are correct.
import random
import math


class Player:
    def __init__(self, name):
        self.name = name
        self.secret = 0


class SecretHolder(Player):
    def __init__(self):
        super().__init__("secret holder")

    def pick_a_number(self):
        self.secret = random.randint(1, 100)
        return self.secret

    def get_cost(self, guess):  # COST/LOSS/ERROR-RATE
        return guess - self.secret  # return the distance


class Guesser(Player):

    def __init__(self):
        super().__init__("guesser")
        self.guess_theta = 50
        self.step_alpha = 5  # Learning Rate - Alpha

    def get_guess_theta(self):
        return self.guess_theta

    def apply_cost(self, cost):  # LEARN
        if cost > 0:  # TOO HIGH - POSITIVE
            self.guess_theta -= self.step_alpha
        if cost < 0:  # TOO LOW - NEGATIVE
            self.guess_theta += self.step_alpha


class Game:
    def __init__(self):
        self.guesser = Guesser()
        self.secret_holder = SecretHolder()

    def play_gradient_decent(self):
        secret_goal = self.secret_holder.pick_a_number()

        feedback_cost = -99999999
        epochs = 0
        good_enough = self.guesser.step_alpha

        while abs(feedback_cost) > good_enough and epochs < 1000:
            guess = self.guesser.get_guess_theta()
            feedback_cost = self.secret_holder.get_cost(guess)
            self.guesser.apply_cost(feedback_cost)
            epochs += 1
            print(epochs, self.guesser.guess_theta, feedback_cost, secret_goal)


g = Game()
g.play_gradient_decent()

# NUMBER LINE - DISTANCE IS THE DIFFERENCE
# -3 -2 -1 0 1 2 3
