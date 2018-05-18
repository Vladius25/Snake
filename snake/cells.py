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
        if game.snake.need_reverse:
            self.time_to_live = game.snake.len - self.time_to_live + 2

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

class DeathFoodCell(FoodCell):
    color = 'red'

    def __init__(self, time_to_live = 50):
        self.time_to_live = time_to_live

    def on_bump(self, game):
        game.is_dead = True
        game.field.set_cell(*game.deathfood, None) 

    def update(self, game):
        if self.time_to_live == 0:
            game.spawn_deathfood()
            return None
        return DeathFoodCell(self.time_to_live - 1)


class PoisonFoodCell(FoodCell):
    color = 'brown'

    def on_bump(self, game):
        self.is_eaten = True
        game.snake.len -= 1
        if game.snake.len == 0:
            game.is_dead = True
            game.is_eaten = True
            game.field.update(game)
        else:
            game.spawn_poisonfood()

class DeathWallCell(Cell):
    color = 'grey'
    
    def on_bump(self, game):
        game.is_dead = True

class ElasticWallCell(Cell):
    color = 'purple'

    def on_bump(self, game):
        game.snake.len += 1
        game.turn(game.snake.OPPOSITE[game.snake.direction])
        game.snake.len -= 1

class TeleportWallCell(Cell):
    color = 'blue'

    def on_bump(self, game):
        if(game.snake.head[1] == 0):
            game.snake.head = (game.snake.head[0], game.field.width - 2) 
            game.turn('left')
        else:
            game.snake.head = (game.snake.head[0], 1) 
            game.turn('right')
        


        
