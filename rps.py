import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = 0
    their_move = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move


class RandomPlayer(Player):
    def move(self):
        move = random.choice(moves)
        return move


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, paper, scissors? > ").lower()
            if move in moves:
                break
        return move


class ReflectPlayer(Player):
    def move(self):
        if self.their_move == 0:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == 0:
            return 'scissors'
        elif self.my_move == moves[0]:
            return moves[1]
        elif self.my_move == moves[1]:
            return moves[2]
        elif self.my_move == moves[2]:
            return moves[0]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# This text_color code function definition was given
# by a mentor that review
# my adventure_game project and he suggested me to use
# this code to give color to my text when it displays.
def text_color(message, color, background=False):
    soc = '\33[48;5;' if background else '\33[38;5;'
    eoc = '\033[0m'
    return f"{soc}{color}m{message}{eoc}"


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.points1 = 0
        self.points2 = 0
        self.points_tie = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"You played {move1}")
        print(f"Opponent played {move2}")

        if move1 == move2:
            print(text_color("--TIE--", 222))
            self.points_tie += 1
        elif beats(move1, move2) is True:
            print(text_color("--PLAYER 1 WINS--", 155))
            self.points1 += 1
        elif beats(move1, move2) is False:
            print(text_color("--PLAYER 2 WINS--", 160))
            self.points2 += 1

        print(f"Player 1: {self.points1}  Player2: {self.points2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print(text_color("Rock Paper Scissors, Go!", 222))
        while True:
            round = self.points1 + self.points2 + self.points_tie + 1
            print(text_color(f"\nRound {round} --", 87))
            self.play_round()
            if self.points1 == self.points2 + 3:
                print(text_color("\n--PLAYER 1 WINS--", 155))
                print("FINAL SCORE")
                print(f"PLAYER 1: {self.points1} point(s)")
                print(f"PLAYER 2: {self.points2} point(s)")
                print("Game over!")
                break
            elif self.points2 == self.points1 + 3:
                print(text_color("\n--PLAYER 2 WINS--", 160))
                print("FINAL SCORE")
                print(f"PLAYER 1: {self.points1} point(s)")
                print(f"PLAYER 2: {self.points2} point(s)")
                print("Game over!")
                break


players = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]
main_player = random.choice(players)

if __name__ == '__main__':
    game = Game(HumanPlayer(), main_player)
    game.play_game()
