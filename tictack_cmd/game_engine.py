import random


# Game fields, it's array of chars [0-8], for ex.: [x,'','','','','',o], where: x - X, o - O, '' - empty cell.
class GameEngine():
    EMPTY_CELL = ''
    X_CELL = 'x'
    O_CELL = 'o'

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
                self.game_field_array[index] = self.O_CELL
                break

    def makePlayerStep(self, cell_index):
        if self.game_field_array[cell_index] == self.EMPTY_CELL:
            self.game_field_array[cell_index] = self.X_CELL

    def isWinnerDefined(self):
        if self.game_field_array[0] == self.X_CELL and self.game_field_array[1] == self.X_CELL and self.game_field_array[2] == self.X_CELL:
            return (True, self.X_CELL)
        if self.game_field_array[3] == self.X_CELL and self.game_field_array[4] == self.X_CELL and self.game_field_array[5] == self.X_CELL:
            return (True, self.X_CELL)
        if self.game_field_array[6] == self.X_CELL and self.game_field_array[7] == self.X_CELL and self.game_field_array[8] == self.X_CELL:
            return (True, self.X_CELL)
        if self.game_field_array[0] == self.X_CELL and self.game_field_array[3] == self.X_CELL and self.game_field_array[6] == self.X_CELL:
            return (True, self.X_CELL)
        if self.game_field_array[1] == self.X_CELL and self.game_field_array[4] == self.X_CELL and self.game_field_array[7] == self.X_CELL:
            return (True, self.X_CELL)
        if self.game_field_array[2] == self.X_CELL and self.game_field_array[5] == self.X_CELL and self.game_field_array[8] == self.X_CELL:
            return (True, self.X_CELL)
        if self.game_field_array[0] == self.X_CELL and self.game_field_array[4] == self.X_CELL and self.game_field_array[8] == self.X_CELL:
            return (True, self.X_CELL)
        if self.game_field_array[2] == self.X_CELL and self.game_field_array[4] == self.X_CELL and self.game_field_array[6] == self.X_CELL:
            return (True, self.X_CELL)
        if self.game_field_array[0] == self.O_CELL and self.game_field_array[1] == self.O_CELL and self.game_field_array[2] == self.O_CELL:
            return (True, self.O_CELL)
        if self.game_field_array[3] == self.O_CELL and self.game_field_array[4] == self.O_CELL and self.game_field_array[5] == self.O_CELL:
            return (True, self.O_CELL)
        if self.game_field_array[6] == self.O_CELL and self.game_field_array[7] == self.O_CELL and self.game_field_array[8] == self.O_CELL:
            return (True, self.O_CELL)
        if self.game_field_array[0] == self.O_CELL and self.game_field_array[3] == self.O_CELL and self.game_field_array[6] == self.O_CELL:
            return (True, self.O_CELL)
        if self.game_field_array[1] == self.O_CELL and self.game_field_array[4] == self.O_CELL and self.game_field_array[7] == self.O_CELL:
            return (True, self.O_CELL)
        if self.game_field_array[2] == self.O_CELL and self.game_field_array[5] == self.O_CELL and self.game_field_array[8] == self.O_CELL:
            return (True, self.O_CELL)
        if self.game_field_array[0] == self.O_CELL and self.game_field_array[4] == self.O_CELL and self.game_field_array[8] == self.O_CELL:
            return (True, self.O_CELL)
        if self.game_field_array[2] == self.O_CELL and self.game_field_array[4] == self.O_CELL and self.game_field_array[6] == self.O_CELL:
            return (True, self.O_CELL)
        return (False, "")

    def checkCorrectInput(self, cell_index):
        return self.game_field_array[cell_index] == self.EMPTY_CELL

game_engine = GameEngine()
