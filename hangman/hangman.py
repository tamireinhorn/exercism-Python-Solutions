# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'
 

class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.__status = STATUS_ONGOING
        self.__word = word 
        self.__masked_word = '_' * len(word)

    def guess(self, char):
        if self.remaining_guesses < 0 or self.__status == STATUS_WIN:
            raise ValueError("The game has already ended.")
        if char in self.__word and char not in self.__masked_word:
           indices = [index for index, character in enumerate(self.__word) if character == char ]
           listed_word = list(self.__masked_word)
           for index in indices:
               listed_word[index] = char
           self.__masked_word = ''.join(listed_word)
        else:
           self.remaining_guesses -= 1
        if self.__masked_word == self.__word:
           self.__status = STATUS_WIN
        elif self.remaining_guesses == 0:
           self.__status = STATUS_LOSE
 
    def get_masked_word(self):
        return self.__masked_word

    def get_status(self):
        return self.__status
