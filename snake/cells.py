class Cell:
    color = 'black'

    def update(self, game):
        return self

    def on_bump(self, game):
        pass


class SnakeCell(Cell):
    color = 'green'

    def __init__(self, time_to_live):
        self.time_to_live = time_to_live

    def update(self, game):
        if self.time_to_live == 1:
            return None
        return SnakeCell(self.time_to_live - 1)

    def on_bump(self, game):
        game.is_dead = True


class FoodCell(Cell):
    color = 'yellow'

    def __init__(self):
        self.is_eaten = False

    def on_bump(self, game):
        self.is_eaten = True
        game.snake.len += 1
        game.score += 1
        game.spawn_food()

    def update(self, game):
        return None if self.is_eaten else self


class DeathWallCell(Cell):
    color = 'grey'

    def on_bump(self, game):
        game.is_dead = True
