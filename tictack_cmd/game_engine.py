

# Game fields, it's array of chars [0-8], for ex.: [x,e,e,e,e,e,o], where: x - X, o - O, e - empty cell.
class GameEngine():
    def __init__(self):
        self.game_field_array =  ['', '', '', '', '', '', '', '', '']

    def resetGameField(self):
        self.game_field_array = ['', '', '', '', '', '', '', '', '']

    def makeComputerStep(self):
        pass

    def makePlayerStep(self, cell_index):
        self.game_field_array[cell_index] = 'x'

    def getGameContext(self):
        pass

