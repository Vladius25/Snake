class Cell:
    color = 'black'

    def update(self, game):
        return self

    def on_bump(self, game, snake):
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

    def on_bump(self, game, snake):
        game.is_dead = True

class AngrySnakeCell(SnakeCell):
    color = 'dark_green'

    def update(self, game):
        if game.snake.need_reverse:
            self.time_to_live += 1

        if self.time_to_live == 1:
            return None

        return AngrySnakeCell(self.time_to_live - 1)


class FoodCell(Cell):
    color = 'yellow'

    def __init__(self):
        self.is_eaten = False

    def on_bump(self, game, snake):
        self.is_eaten = True
        snake.len += 1
        snake.score += 1
        game.spawn_food()

    def update(self, game):
        return None if self.is_eaten else self

class DeathFoodCell(FoodCell):
    color = 'red'

    def __init__(self, time_to_live = 50):
        self.time_to_live = time_to_live

    def on_bump(self, game, snake):
        game.is_dead = True
        game.field.set_cell(*game.deathfood, None) 

    def update(self, game):
        if self.time_to_live == 0:
            game.spawn_deathfood()
            return None
        return DeathFoodCell(self.time_to_live - 1)


class PoisonFoodCell(FoodCell):
    color = 'brown'

    def on_bump(self, game, snake):
        self.is_eaten = True
        snake.len -= 1
        if snake.len == 0:
            game.is_dead = True
            game.is_eaten = True
            game.field.update(game)
        else:
            game.spawn_poisonfood()

class DeathWallCell(Cell):
    color = 'grey'
    
    def on_bump(self, game, snake):
        game.is_dead = True

class ElasticWallCell(Cell):
    color = 'purple'

    def on_bump(self, game, snake):
        snake.len += 1
        game.turn(snake.OPPOSITE[snake.direction])
        snake.len -= 1

class TeleportWallCell(Cell):
    color = 'blue'

    def on_bump(self, game, snake):
        if(snake.head[1] == 0):
            snake.head = (snake.head[0], game.field.width - 2) 
            game.turn('left')
        else:
            snake.head = (snake.head[0], 1) 
            game.turn('right')
        


        
