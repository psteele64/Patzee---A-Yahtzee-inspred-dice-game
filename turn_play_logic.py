from os import system, name

import random
import os
from score_logic import Scoring
from hand_scoring import Score_hand
from os import system, name
from screen_clr_util import screen_clear

class Turn_logic:
    """Class for a functioning turn per instance of player. Expects nothing but takes calls from the player instance but modifies the dictionary and calls functions from ScoreKeeper """

    def __init__(self):
        """Gives the turn class the number of rolls, dice and Turn_logic to start with. 
        Also gives empty lists for roll results and dice chosen to keep and kept dice counter.
        Also points to the board and score instances.
        """
        self.num_dice = 5
        self.num_rolls = 3
        self.roll_result = []
        self.chosen_dice = []
        self.kept_count = 0
        self.turn_count = 0
        self.score_board = Score_hand()
        self.score = Scoring(self.roll_result, self.score_board)

    def roll(self):
        """Initializes a roll for player instances. Prints a list of randomly selected dice and calls the kept dice function after roll.
        Also decrements number of rolls and passes to Score after roll is complete.
        """
        if self.num_rolls > 0:
            for _ in range(self.num_dice - self.kept_count):
                self.roll_result.append(random.randint(1, 6))
            self.num_rolls -= 1
            if self.num_rolls > 1:
                print(f"{self.num_rolls} rolls left\n")
            elif self.num_rolls == 1:
                print(f"{self.num_rolls} roll left\n")
            else:
                pass
            # random.shuffle(self.roll_result) when developed further
            print(f"\nCurrent roll:\n{self.roll_result}\n")
            if self.num_rolls > 0:
                self.roll_reset()
            else:
                Scoring(self.roll_result, self.score_board).score_time_display()
                # self.score.score_time_display()
                self.end_of_turn()

    def roll_reset(self):
        """Reset chosen dice, kept count and then rolls again. Contains the Try/Except for kept dice.Asks player if they want to end turn and score hand"""
        while True:
            stop_score = input("\nEnter 'y' to end turn and score hand now or\n\npress ENTER to continue and choose the dice you want to keep\n\n      'y' or 'ENTER: ")
            if stop_score == "y":
                screen_clear()
                Scoring(self.roll_result, self.score_board).score_time_display()
                self.end_of_turn()
                break
            elif stop_score == "":
                screen_clear()
                print(f"\nCurrent roll:\n{self.roll_result}\n")
                self.chosen_dice = []
                self.kept_count = 0
                try:
                    self.ask_kept_dice()
                except (IndexError, ValueError):
                    print("""\nPlease enter valid space-separated number (1 2 3 4 5) for each position you'd like to keep\n""")
                    self.ask_kept_dice()
                self.roll()
                break
            else:
                print("\nInvalid choice!\n")
                screen_clear()
                continue

    def end_of_turn(self):
        """Increments the turn counter. Then resets chosen dice, kept count, roll count, roll result and calls roll for next turn
        For multiplayer this then lead to the turn change to the next player"""
        self.turn_count += 1
        self.chosen_dice = []
        self.kept_count = 0
        self.num_rolls = 3
        self.roll_result = []
        screen_clear()

    def ask_kept_dice(self):
        """Ask the user which dice they would like to keep to reroll. It then grooms the input to append desired dice to chosen dice
        and increments the kept count to let Roll readjust the amount of dice to roll.
        Clears the terminal and prints the kept dice which is now the roll result to add to the next roll"""
        while True:
            if self.turn_count < 3:
                try:
                    choice = [int(i)for i in (input("Which would you like to keep?\nChoose from (1 2 3 4 5)\n").strip().split())]
                except (ValueError, IndexError):
                    print("""\nPlease enter valid space-separated number (1 2 3 4 5) for each position you'd like to keep\n""")
                    continue
            else:
                try:
                    choice = [int(i)for i in (input("Which would you like to keep?\n").strip().split())]
                except (ValueError, IndexError):
                    print("""\nPlease enter valid space-separated number (1 2 3 4 5) for each position you'd like to keep\n""")
                    continue
                """Take the chosen dice by index and return {result} as a new list
                New list 'choice' is then """
            break
        for i in list(set(choice)):
            self.chosen_dice.append(self.roll_result[i - 1])
            self.kept_count += 1
        self.roll_result = self.chosen_dice
        screen_clear()
        print(f"You kept these {self.roll_result}\n")
