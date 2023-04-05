#1.Импортируем необходимые модули и устанавливаем размер игрового окна:
import pygame, sys
import random

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake')

#2.Создаем класс для змеи:
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)
        
    def get_head_position(self):
        return self.positions[0]
        
    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point
        
    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x*GRID_SIZE)) % WINDOW_WIDTH, (cur[1] + (y*GRID_SIZE)) % WINDOW_HEIGHT)
        if new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
        
    def reset(self):
        self.length = 1
        self.positions = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

#3.Создаем класс для еды:
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position()
        
    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRID_SIZE, random.randint(0, GRID_HEIGHT-1) * GRID_SIZE)

#4.Определяем константы для направлений и размера сетки:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH / GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT / GRID_SIZE

#5.Определяем функцию для рисования сетки:
def draw_grid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (84, 194, 205), rr)

#6.Определяем функцию для рисования змеи:
def draw_snake(surface, snake):
    for p in snake.positions:
        r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, snake.color, r)
        r = pygame.Rect((p[0]+4, p[1]+4), (12, 12))
        pygame.draw.rect(surface, (93, 216, 228), r)

#7.Определяем функцию для рисования еды:
def draw_food(surface, food):
    r = pygame.Rect((food.position[0], food.position[1]), (GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(surface, food.color, r)
    pygame.draw.rect(surface, (93, 216, 228), r, 1)

#8.Определяем функцию для обновления игры:
def update():
    global snake, food, score, level, speed
    snake.move()
    if snake.get_head_position() == food.position:
        snake.length += 1
        score += 10
        food.randomize_position()
        if score % 50 == 0:
            level += 1
            speed += 1
    draw_grid(WINDOW)
    draw_snake(WINDOW, snake)
    draw_food(WINDOW, food)
    pygame.display.set_caption(f'Snake  | Score: {score} | Level: {level}')

#9.Определяем функцию для проверки столкновения со стеной:
def check_collision_with_wall(snake):
    return (snake.get_head_position()[0] in (0, GRID_WIDTH-1) or
            snake.get_head_position()[1] in (0, GRID_HEIGHT-1))


#10.Определяем функцию для проверки столкновения со змеей:
def check_collision_with_self(snake):
    return snake.get_head_position() in snake.positions[1:]

#11.Определяем функцию для изменения скорости:
def set_difficulty(level, speed):
    if level == 1:
        speed = 10
    elif level == 2:
        speed = 12
    elif level == 3:
        speed = 15
    else:
        speed = 20
    return speed

#12.Определяем функцию для запуска игры:
def run_game():
    global snake, food, score, level, speed
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    score = 0
    level = 1
    speed = 10

    while True:
        clock.tick(speed)
        snake.turn(get_direction(snake.direction))
        update()
        speed = set_difficulty(level, speed)

        if check_collision_with_wall(snake) or check_collision_with_self(snake):
            pygame.time.delay(1000)
            snake.reset()
            score = 0
            level = 1
            speed = 10

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

#13.Определяем функцию для получения направления движения:
def get_direction(current_direction):
    next_direction = current_direction
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                next_direction = UP
            elif event.key == pygame.K_DOWN:
                next_direction = DOWN
            elif event.key == pygame.K_LEFT:
                next_direction = LEFT
            elif event.key == pygame.K_RIGHT:
                next_direction = RIGHT
    return next_direction

#14.Вызываем функцию run_game() для запуска игры:
if __name__ == '__main__':
    run_game()
