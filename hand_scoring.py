class Score_hand:
    """This is the class for keeping track of the active scores and the formulation of what the categories are.
    It keeps the algorithms for the upper score bonus, end of game score and displaying the actively entered categories during a given turn"""

    def __init__(self):
        """Initializes the 'Score_hand' class to have a dictionary for each scoring category defaulted to None as well as the score_board_upper_list tuple"""
        self.score_board_dict = {
            "ones": None,
            "twos": None,
            "threes": None,
            "fours": None,
            "fives": None,
            "sixes": None,
            "three of a kind": None,
            "four of a kind": None,
            "full house": None,
            "small straight": None,
            "large straight": None,
            "patzee": None,
            "chance": None,
            "patzee bonus": None,
            "upper bonus": None,
        }
        self.score_board_upper_list = (
            "ones",
            "twos",
            "threes",
            "fours",
            "fives",
            "sixes",
        )

    def score_bonus(self):
        """Computes and updates the dict with the bonus if any and return_logic 35 or 0 points to the upper bonus dict value"""
        if (
            sum(
                score
                for category, score in self.score_board_dict.items()
                if category in self.score_board_upper_list) >= 63
        ):
            self.score_board_dict["upper bonus"] = 35
        else:
            self.score_board_dict["upper bonus"] = 0
        if self.score_board_dict["patzee bonus"] is None:
            self.score_board_dict["patzee bonus"] = 0

    def end_of_game_score(self):
        """Computes the end of game score including bonus for each player instance call"""
        self.score_bonus()
        self.score_final = sum(score for category, score in self.score_board_dict.items())
        return self.score_final

    def display_active_categories(self):
        """Calculates the actively non None scores for each player instance and 
        is called by turn to display when needing to choose a category for scoring.
        no_score counter increments with each loop iteration. If all values are 'None'
        prints 'None yet...' instead of the used scoring categories """
        print("\nYou've scored in these categories so far:\n")
        no_score = 0
        for category, score in self.score_board_dict.items():
            if score is not None:
                print(category.title() + ": " + str(score))
                no_score += 1
        if no_score == 0:
            print("None yet....")

    def display_available_categories(self):
        """Computes the remaining available categories to select from and 
        displays them after already scored categories"""
        print("\nChoose from these remaining categories: ")
        for category, score in self.score_board_dict.items():
            if score is None and category not in ["patzee bonus", "upper bonus"]:
                print(category.title())
        print()
