from snake_game.Segment import Segment
from snake_game import constants as c
import pygame


class Snake:

    def __init__(self, is_drawing = True):
        self.segments = []
        self.segments.append(Segment(1, 0))
        self.segments.append(Segment(0, 0))
        self.direction = c.RIGHT
        self.alive = True
        self.is_drawing = is_drawing
        self.draw_group = None
        if is_drawing:
            self.draw_group = pygame.sprite.Group()
            self.draw_group.add(self.segments[0])
            self.draw_group.add(self.segments[1])

    def forward(self):
        first_segment = self.segments[0]
        last_segment = self.segments[len(self.segments)-1]
        self.segments.remove(last_segment)
        if self.is_drawing:
            self.draw_group.remove(last_segment)
        if self.direction == c.TOP:
            new_segment = Segment(first_segment.x, first_segment.y-1)
        elif self.direction == c.RIGHT:
            new_segment = Segment(first_segment.x+1, first_segment.y)
        elif self.direction == c.BOTTOM:
            new_segment = Segment(first_segment.x, first_segment.y+1)
        else:
            new_segment = Segment(first_segment.x-1, first_segment.y)

        # si toca los bordes
        if new_segment.x <= -1 or new_segment.x >= c.BOX_SIZE \
            or new_segment.y <= -1 or new_segment.y >= c.BOX_SIZE:
            self.alive = False

        for segment in self.segments:
            if segment.x == new_segment.x and segment.y == new_segment.y:
                self.alive = False
                break

        self.segments.insert(0, new_segment)
        if self.is_drawing:
            self.draw_group.add(new_segment)
        return last_segment

    def add_segment(self, segment):
        self.segments.append(segment)
        if self.is_drawing:
            self.draw_group.add(segment)
