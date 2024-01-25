class State:
    def __init__(self, item = ENDED, step = 0):
        self.item = item                        # Item of the test in the current State
        self.step = step                        # Step of the current test item
        self.forward_numbers = 0                # True if has remembered straight list of numbers
        self.backward_numbers = 0               # True if has remembered reversed list of numbers
        self.f_words = []                       # List of valid words starting with F
        self.f_start_time = None                # Timestamp of when the F words step started, to count 1 min
        self.letters_last_time = None           # Timestamp of last letter response, in order to measure reaction time
        self.score = 0                          # Overall score of the current test
        self.calculations = []                  # List of calculated substractions of -7 starting from 100
        self.letter_mistakes = 29               # Number of letter mistakes (say yes when it's not A, etc)
        self.first_sentence = 0                 # 1 if user remembered first sentence perfectly
        self.second_sentence = 0                # 1 if user remembered second sentence perfectly
        self.transport = 0                      # 1 if the user is able to tell the category of train and bike
        self.measure = 0                        # 1 if the user is able to tell the category of ruler and clock
        self.unclued_recalls = []               # Words remembered without category clue
        self.clued_recalls = []                 # Words remembered with category clue
        self.choice_recalls = []                # Words remembered with multiple choice clue
        self.day = 0                            # Day of the month stated by user
        self.month = ""                         # Current month stated by user
        self.week = ""                          # Day of the week stated by user
        self.year = 0                           # Current year stated by user
        self.afaga = 0                          # True if user is able to say that we are in Afaga
        self.vigo = 0                           # True if user is able to say that we are in Vigo city
        self.date = ""                          # Date of test administration
        self.study_years = 0                    # Number of years of study (add 1 point if less than 12 years)
        self.user_id = 0                        # User ID number

    def set(self, item = ENDED, step = 0):
      self.item = item
      self.step = step
