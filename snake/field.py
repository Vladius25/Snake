import random
from .cells import SnakeCell

class Field:
    def __init__(self,  width=20, height=20):
        self.width = width
        self.height = height

        self._cells = [[None for j in range(width)] for i in range(height)]

    def contains_cell(self, y, x):
        return (0 <= y < self.height) and (0 <= x < self.width)

    def is_empty(self, y, x):
        if not self.contains_cell(y, x):
            raise ValueError('Cell ({0}, {1}) is outside of field'.format(y, x))
        return self._cells[y][x] is None

    def get_random_empty_cell(self):
        while True:
            y, x = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            if self.is_empty(y, x):
                return y, x

    def set_cell(self, y, x, cell):
        if not self.contains_cell(y, x):
            raise ValueError('Cell ({0}, {1}) is outside of field'.format(y, x))
        self._cells[y][x] = cell

    def get_cell(self, y, x):
        if not self.contains_cell(y, x):
            raise ValueError('Cell ({0}, {1}) is outside of field'.format(y, x))
        return self._cells[y][x]

    def update(self, game):
        for y in range(self.height):
            for x in range(self.width):
                cell = self._cells[y][x]
                if game.snake.need_reverse == True and type(self._cells[y][x]) == SnakeCell and self._cells[y][x].time_to_live == 1: 
                    game.snake.head = y, x
                if cell is not None:
                    self._cells[y][x] = cell.update(game)
