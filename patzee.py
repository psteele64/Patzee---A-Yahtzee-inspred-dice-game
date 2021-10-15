from turn_play_logic import Turn_logic
from score_logic import Scoring
from hand_scoring import Score_hand
from os import system, name
from banner import show_banner
from screen_clr_util import screen_clear
from time import sleep

game_over = False
screen_clear()
show_banner()
sleep(3)
screen_clear()

class Player(Turn_logic, Scoring, Score_hand):
    """Initializes a player instance and gives instance of each other class required to play. Expects Turn_logic Score and Score_hand instance."""

    def __init__(self):
        """Initializes the player class to inherit from the Turn_logic, Score and Score_hand classes"""
        Turn_logic.__init__(self)
        Scoring.__init__(self, self.roll_result, self.score_board)
        Score_hand.__init__(self)


player1 = Player()
player2 = Player()


def ask_for_players():
    """Asks how many players are playing and expects an answer of 1 or 2 at the moment. Recalls itself when answer isn't an expected option"""
    try:
        player_count = int(
            input("How many players are there? Options: 1 or 2\n"))
        if player_count == 1:
            one_player(game_over, player1)
        elif player_count == 2:
            two_player(game_over, turn_order, player1, player2)
        else:
            print("Please enter a valid number of players")
            ask_for_players()
    except ValueError:
        print("You've entered an invalid player count")
        ask_for_players()


def one_player(game_over, player1):
    """Starts the game for one player functionality. Expects game_over and a player1 instance"""
    screen_clear()
    while not game_over:
        while True:
            input("\nPress 'Enter' key' to Roll:")
            break
        player1.roll()

        print(f"Turn #{player1.turn_count + 1}")
        if player1.turn_count == 13:
            print("-------------")
            print("Final Scores!")
            print("-------------")
            print()
            print(
                f"You ended with a score of {player1.score_board.end_of_game_score()}!"
            )
            enter = input("Thanks for playing!")
            if enter == "":
                game_over = True
                exit()


turn_order = 0


def two_player(game_over, turn_order, player1, player2):
    #     """Starts the game for two player functionality. Expects game_over, turn_order and two player instances"""
    screen_clear()
    while not game_over:
        if turn_order == 0:
            print(f"Turn #{player1.turn_count + 1} for Player 1")
            player1.roll()
        else:
            print(f"Turn #{player2.turn_count + 1} for Player 2")
            player2.roll()
        if player1.turn_count == 13 and player2.turn_count == 13:
            print("-------------")
            print("Final Scores!")
            print("-------------")
            print()
            print(
                f"Player 1's score is: {player1.score_board.end_of_game_score()}\nPlayer 2's score is: {player2.score_board.end_of_game_score()}"
            )
            enter = input("Thanks for playing!")
            if enter == "":
                game_over = True
                exit()
        turn_order += 1
        turn_order = turn_order % 2


ask_for_players()
