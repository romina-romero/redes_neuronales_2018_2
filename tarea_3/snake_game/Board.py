from snake_game.Snake import Snake
from snake_game.Food import Food
from snake_game import constants as c
import random
import pygame


class Board:

    def __init__(self, size, is_drawing = True):

        self.size = size
        self.snake = Snake(is_drawing)
        self.food = Food(random.randint(0, self.size-1), random.randint(0, self.size-1))
        self.is_drawing = is_drawing
        if is_drawing:
            self.snake.draw_group.add(self.food)

    def forward(self):

        last_segment = self.snake.forward()

        if self.snake.segments[0].x == self.food.x and self.snake.segments[0].y == self.food.y:
            self.snake.add_segment(last_segment)
            if self.is_drawing:
                self.snake.draw_group.remove(self.food)
            self.food = Food(random.randint(0, self.size-1), random.randint(0, self.size-1))
            if self.is_drawing:
                self.snake.draw_group.add(self.food)

    def change_direction(self, direction):

        first_segment = self.snake.segments[0]
        if len(self.snake.segments) > 1:
            second_segment = self.snake.segments[1]
            if direction == c.RIGHT or direction == c.LEFT:
                if second_segment.y == first_segment.y:
                    return
            else:
                if second_segment.x == first_segment.x:
                    return

        self.snake.direction = direction

    def rotate(self, positive = True):
        if positive:
            if self.snake.direction == c.TOP: self.snake.direction = c.LEFT
            elif self.snake.direction == c.LEFT: self.snake.direction = c.BOTTOM
            elif self.snake.direction == c.BOTTOM: self.snake.direction = c.RIGHT
            else: self.snake.direction = c.TOP
        else:
            if self.snake.direction == c.TOP: self.snake.direction = c.RIGHT
            elif self.snake.direction == c.RIGHT: self.snake.direction = c.BOTTOM
            elif self.snake.direction == c.BOTTOM: self.snake.direction = c.LEFT
            else: self.snake.direction = c.TOP

    def food_distance(self):
        dist = self.size
        if self.snake.direction==c.TOP and \
            self.snake.segments[0].x == self.food.x and \
            self.snake.segments[0].y > self.food.y:
            dist = self.snake.segments[0].y - self.food.y

        elif self.snake.direction==c.LEFT and \
            self.snake.segments[0].y == self.food.y and \
            self.snake.segments[0].x > self.food.x:
            dist = self.snake.segments[0].x - self.food.x

        elif self.snake.direction == c.BOTTOM and \
                self.snake.segments[0].x == self.food.x and \
                self.snake.segments[0].y < self.food.y:
            dist = -self.snake.segments[0].y + self.food.y

        elif self.snake.direction == c.RIGHT and \
                self.snake.segments[0].y == self.food.y and \
                self.snake.segments[0].x < self.food.x:
            dist = -self.snake.segments[0].x + self.food.x

        return dist

    def obs_distance(self):
        dist = self.size
        if self.snake.direction == c.TOP:
            dist = self.snake.segments[0].y
            for i in range(1, len(self.snake.segments)):
                if self.snake.segments[i].x == self.snake.segments[0].x and\
                   self.snake.segments[i].y > self.snake.segments[0].y:
                    dist = min(dist, self.snake.segments[i].y - self.snake.segments[0].y)

        elif self.snake.direction == c.LEFT:
            dist = self.snake.segments[0].x
            for i in range(1, len(self.snake.segments)):
                if self.snake.segments[i].y == self.snake.segments[0].y and\
                   self.snake.segments[i].x > self.snake.segments[0].x:
                    dist = min(dist, self.snake.segments[i].x - self.snake.segments[0].x)

        elif self.snake.direction == c.BOTTOM:
            dist = self.size - self.snake.segments[0].y
            for i in range(1, len(self.snake.segments)):
                if self.snake.segments[i].x == self.snake.segments[0].x and\
                   self.snake.segments[i].y < self.snake.segments[0].y:
                    dist = min(dist, -self.snake.segments[i].y + self.snake.segments[0].y)

        elif self.snake.direction == c.RIGHT:
            dist = self.size - self.snake.segments[0].x
            for i in range(1, len(self.snake.segments)):
                if self.snake.segments[i].y == self.snake.segments[0].y and\
                   self.snake.segments[i].x < self.snake.segments[0].x:
                    dist = min(dist, -self.snake.segments[i].x + self.snake.segments[0].x)
        return dist

    def draw(self):
        if not self.is_drawing:
            print("No se habilito el dibujo")
            return
        screen = pygame.display.set_mode([c.WINDOW_SIZE, c.WINDOW_SIZE])
        screen.fill(c.BLACK)
        pygame.draw.rect(screen, c.RED, (0, 0, c.SEGMENT_MARGIN, c.WINDOW_SIZE))
        pygame.draw.rect(screen, c.RED, (0, 0, c.WINDOW_SIZE, c.SEGMENT_MARGIN))
        pygame.draw.rect(screen, c.RED, (c.WINDOW_SIZE-c.SEGMENT_MARGIN, 0, c.SEGMENT_MARGIN, c.WINDOW_SIZE))
        pygame.draw.rect(screen, c.RED, (0, c.WINDOW_SIZE-c.SEGMENT_MARGIN, c.WINDOW_SIZE,
                                         c.SEGMENT_MARGIN))
        self.snake.draw_group.draw(screen)
