import pygame
import sys
import random

pygame.init()

# 游戏区域设置
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE
GRID_COLOR = (50, 50, 50)

# 蛇和食物颜色
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

# 定义蛇的方向
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 游戏速度
FPS = 4

# 初始化窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("贪吃蛇")

def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, FOOD_COLOR, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def get_random_location():
    return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

def main():
    clock = pygame.time.Clock()

    # 初始化蛇的位置和初始长度
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 4)]
    snake_direction = RIGHT

    # 初始化食物位置
    food = get_random_location()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != DOWN:
                    snake_direction = UP
                elif event.key == pygame.K_DOWN and snake_direction != UP:
                    snake_direction = DOWN
                elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                    snake_direction = LEFT
                elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                    snake_direction = RIGHT

        # 蛇头移动
        head_x, head_y = snake[0]
        new_head = (head_x + snake_direction[0], head_y + snake_direction[1])

        # 判断游戏结束的条件
        if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or new_head in snake:
            pygame.quit()
            sys.exit()

        snake.insert(0, new_head)

        # 判断是否吃到食物
        if new_head == food:
            food = get_random_location()
        else:
            snake.pop()

        # 绘制游戏界面
        screen.fill((0, 0, 0))
        draw_grid()
        draw_snake(snake)
        draw_food(food)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
