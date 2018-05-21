from .field import Field
from .cells import SnakeCell, FoodCell, DeathWallCell, ElasticWallCell, TeleportWallCell, PoisonFoodCell, DeathFoodCell, AngrySnakeCell
from .bfs import Bfs

class SnakeState:
    TURNS = {
        'up':    (-1, 0),
        'down':  (1, 0),
        'left':  (0, -1),
        'right': (0, 1),
    }

    OPPOSITE = {
        'up': 'down',
        'down': 'up',
        'left': 'right',
        'right': 'left',
    }

    def __init__(self, head_position, start_length, direction, score = 0, head_color = 'turquoise'):
        self.head = head_position
        self.len = start_length
        self.direction = direction
        self.need_reverse = False
        self.score = score
        self.cell_type = SnakeCell
        self.head_color = head_color

    def turn(self, direction):
        if direction not in self.TURNS.keys():
            raise ValueError('{0} is not a valid side' % direction)
        self.direction = direction

    def get_next_position(self):
        dy, dx = self.TURNS[self.direction]
        return self.head[0] + dy, self.head[1] + dx

    def get_side(self, y, x):
        for direction, pos in self.TURNS.items():
             if pos == (y, x):
                return direction

class AngryState(SnakeState):

    def __init__(self, head_position, start_length, direction, score = 0, head_color = 'indigo'):
        super().__init__(head_position, start_length, direction, score)
        self.cell_type = AngrySnakeCell
        self.head_color = head_color

    def get_next_position(self, y, x, field):
        bfs = Bfs()
        return bfs.get_next(*self.head, y, x, field)


class Game:
    def __init__(self, width=20, height=20):
        self.field = Field(width, height)
        self.snake = SnakeState((1, 2), 2, 'right')
        self.angry = AngryState((height - 2, width - 3), 2, "left")

        self.is_paused = True
        self.is_dead = False

        self.width = width
        self.height = height

        self.init_level()

    def init_level(self):
        self.init_snake(self.snake)
        self.init_snake(self.angry)

        for x in range(self.field.width):
            self.field.set_cell(0, x, ElasticWallCell())
            self.field.set_cell(self.field.width - 1, x, DeathWallCell())

        for y in range(self.field.height):
            self.field.set_cell(y, 0, TeleportWallCell())
            self.field.set_cell(y, self.field.height - 1, TeleportWallCell())

        self.spawn_food()
        self.spawn_poisonfood()
        self.spawn_deathfood()

    def init_snake(self, snake):
            dx = snake.TURNS[snake.direction][1]
            self.field.set_cell(*snake.head, snake.cell_type(time_to_live = snake.len))
            self.field.set_cell(snake.head[0], snake.head[1] - dx, snake.cell_type(time_to_live = snake.len - 1))
            self.field.get_cell(*snake.head).color = snake.head_color

    def spawn_food(self):
        y, x = self.field.get_random_empty_cell()
        self.food = y, x
        self.field.set_cell(y, x, FoodCell())

    def spawn_poisonfood(self):
        y, x = self.field.get_random_empty_cell()
        self.field.set_cell(y, x, PoisonFoodCell())

    def spawn_deathfood(self):
        y, x = self.field.get_random_empty_cell()
        self.deathfood = y, x
        self.field.set_cell(y, x, DeathFoodCell())

    def pause(self):
        self.is_paused = not self.is_paused

    def restart(self, width = 30, height = 30):
        self.is_paused = False
        self.__init__(width, height)

    def turn(self, side):
        if self.snake.direction == self.snake.OPPOSITE[side]:
            self.snake.need_reverse = True
            self.field.update(game=self)
            dx = (1, -1, 0, 0)
            dy = (0, 0, 1, -1)
            y, x = self.snake.head
            for i in range(4):
                if type(self.field.get_cell(y + dy[i], x + dx[i])) == SnakeCell:
                    side = self.snake.get_side(-dy[i], -dx[i])
                    break
            self.snake.need_reverse = False

        self.snake.turn(side)

    def update(self):
        if self.is_paused or self.is_dead:
            return

        if not self.try_move_head():
            self.is_dead = True
            return

        for snake in [self.snake, self.angry]:
            cell = self.field.get_cell(*snake.head)
            if cell is not None:
                cell.on_bump(self, snake)

        if self.is_dead:
            return

        self.field.update(game=self)

        self.field.set_cell(*self.snake.head, SnakeCell(time_to_live=self.snake.len))
        self.field.get_cell(*self.snake.head).color = self.snake.head_color

        self.field.set_cell(*self.angry.head, AngrySnakeCell(time_to_live=self.angry.len))
        self.field.get_cell(*self.angry.head).color = self.angry.head_color

    def try_move_head(self):
        new_y, new_x = self.snake.get_next_position()
        new_angry_y, new_angry_x = self.angry.get_next_position(*self.food, self.field)

        if self.field.contains_cell(new_y, new_x):
            self.snake.head = new_y, new_x
            self.angry.head = new_angry_y, new_angry_x
            return True
        return False