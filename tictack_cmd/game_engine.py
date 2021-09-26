

# Game fields, it's array of chars [0-8], for ex.: [x,e,e,e,e,e,o], where: x - X, o - O, e - empty cell.
import random


class GameEngine():
    EMPTY_CELL = ''

    def __init__(self):
        self.game_field_array = [self.EMPTY_CELL] * 9

    def resetGameField(self):
        self.game_field_array = [self.EMPTY_CELL] * 9

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

    def getGameContext(self):
        pass

    def checkCorrectInput(self, cell_index):
        """
        Check that cell_index is satisfied of criteria: digit / cell of array is not filled / and index between 0 and 9.
        :param cell_input_index: index cell that have to be verified (typed from player).
        :param cells_array:
        :return: True/False
        """
        if self.game_field_array[cell_index] != self.EMPTY_CELL:
            return False
        return True


