class Scoring:
    """Inherits roll result from turn and defines functions for detecting and scoring roll results. Contains algorithms for each scoring category
    to either award points or grant 0 points if a roll does not meet the requirements"""

    def __init__(self, roll_result, score_board):
        """Takes the roll result from patzee.py and uses it for scoring and defines dicts for filtering and applying singleScores and 
        for detecting transferring user category get_scoring_selection into the category_function_dict list of functions. Also sets up the board to be used as a class parameter"""
        self.roll_result = roll_result
        self.singles = {
            "ones": 1,
            "twos": 2,
            "threes": 3,
            "fours": 4,
            "fives": 5,
            "sixes": 6,
        }
        self.category_function_dict = {
            "ones": self.single_die_score,
            "twos": self.single_die_score,
            "threes": self.single_die_score,
            "fours": self.single_die_score,
            "fives": self.single_die_score,
            "sixes": self.single_die_score,
            "three of a kind": self.three_of_a_kind,
            "four of a kind": self.four_of_a_kind,
            "full house": self.full_house,
            "small straight": self.small_straight,
            "large straight": self.large_straight,
            "patzee": self.patzee,
            "chance": self.chance,
        }
        self.score_board = score_board

    def score_time_display(self):
        """Displays the currently attained scores. Then asks user for which category to score roll
        and gives lowercase get_scoring_selection to score filter"""
        print("It's time to score your roll!")
        while True:
            input("\nPress 'Enter' key' to Score:")
            break
        print("Here's your roll again:\n")
        print(self.roll_result)
        self.score_board.display_active_categories()
        self.score_board.display_available_categories()
        self.get_scoring_selection = input(
            "For which category would you like to score?\n"
        ).lower()
        self.scoreFilter(self.get_scoring_selection)

    def scoreFilter(self, get_scoring_selection):
        """Maps the user get_scoring_selection to the dictionary key to feed value of class functions to be called for scoring eligibility"""
        if (
            (self.get_scoring_selection in self.category_function_dict.keys())
            and self.score_board.score_board_dict[f"{self.get_scoring_selection}"]
            == None
        ):
            self.score_board.score_board_dict[
                f"{self.get_scoring_selection}"
            ] = self.category_function_dict[f"{self.get_scoring_selection}"]()
        else:
            print("This selection has been taken already")
            self.score_time_display()

    def single_die_score(self):
        """Parses singles dict then adds sum of the singles roll result to the scoring dictionary"""
        if self.get_scoring_selection in self.singles:
            score = sum(
                i
                for i in self.roll_result
                if i == self.singles[self.get_scoring_selection]
            )
            return score
        else:
            score = 0
            return score
        return score

    def three_of_a_kind(self):
        """Algorithm to detect at least three dice the same"""
        self.roll_result.sort()
        if (
            self.roll_result[0] == self.roll_result[2]
            or self.roll_result[1] == self.roll_result[3]
            or self.roll_result[2] == self.roll_result[4]
        ):
            score = sum(i for i in self.roll_result)
            return score
        else:
            score = 0
            return score

    def four_of_a_kind(self):
        """Algorithm to detect at least four dice the same"""
        self.roll_result.sort()
        if (
            self.roll_result[0] == self.roll_result[3]
            or self.roll_result[1] == self.roll_result[4]
        ):
            score = sum(i for i in self.roll_result)
            return score
        else:
            score = 0
            return score

    def full_house(self):
        """Algorithm to detect three of one number and two of another"""
        self.roll_result.sort()
        if len(set(self.roll_result)) != 2:
            score = 0
            return score
        elif (
            self.roll_result[0] != self.roll_result[3]
            or self.roll_result[1] != self.roll_result[4]
        ):
            score = 25
            return score

    def small_straight(self):
        """Algorithm to detect four sequential dice"""
        self.roll_result.sort()
        if len(set(self.roll_result)) < 4:
            score = 0
            return score
        elif (
            (len(set([1, 2, 3, 4]).intersection(set(self.roll_result))) == 4)
            or (len(set([2, 3, 4, 5]).intersection(set(self.roll_result))) == 4)
            or (len(set([3, 4, 5, 6]).intersection(set(self.roll_result))) == 4)
        ):
            score = 30
            return score
        else:
            score = 0
            return score

    def large_straight(self):
        """Algorithm to detect five sequential dice"""
        self.roll_result.sort()
        if len(set(self.roll_result)) < 5:
            score = 0
            return score
        elif (len(set([1, 2, 3, 4, 5]).intersection(set(self.roll_result))) == 5) or (
            len(set([2, 3, 4, 5, 6]).intersection(set(self.roll_result))) == 5
        ):
            score = 40
            return score
        else:
            score = 0
            return score

    def patzee(self):
        """Algorithm to detect that all five dice are the same"""
        if len(set(self.roll_result)) == 1:
            if (
                self.score_board.score_board_dict["patzee"] != None
                and self.score_board.score_board_dict["patzee"] != 0
            ):
                self.score_board.score_board_dict["patzee bonus"] += 100
                return
            else:
                score = 50
                return score
        else:
            score = 0
            return score

    def chance(self):
        """Algorithm to compute any combination of roll result"""
        score = sum(self.roll_result)
        return score
