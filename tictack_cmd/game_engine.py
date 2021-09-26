import random


# Game fields, it's array of chars [0-8], for ex.: [x,'','','','','',o], where: x - X, o - O, '' - empty cell.
class GameEngine():
    EMPTY_CELL = ''

    def __init__(self):
        self.game_field_array = [self.EMPTY_CELL] * 9
        print("we are here 4")

    def resetGameField(self):
        self.game_field_array = [self.EMPTY_CELL] * 9
        print("we are here 5")

    def makeComputerStep(self):
        indices = [i for i, x in enumerate(self.game_field_array) if x == self.EMPTY_CELL]
        if not indices:
            return
        elif len(indices) == 1:
            idx = indices[0]
            self.game_field_array[idx] = 'o'

        while True:
            index = random.randint(0,8)
            if self.game_field_array[index] == self.EMPTY_CELL:
                self.game_field_array[index] = 'o'
                break

    def makePlayerStep(self, cell_index):
        if self.game_field_array[cell_index] == self.EMPTY_CELL:
            self.game_field_array[cell_index] = 'x'


game_engine = GameEngine()
