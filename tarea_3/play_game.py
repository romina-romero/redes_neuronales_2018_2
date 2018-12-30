import pygame
from snake_game.Board import Board
from snake_game import constants as c

# Call this function so the Pygame library can initialize itself
pygame.init()
board = Board(c.BOX_SIZE)
board.draw()
# Set the title of the window
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()
done = False

i=0
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                board.change_direction(c.LEFT)
            if event.key == pygame.K_RIGHT:
                board.change_direction(c.RIGHT)
            if event.key == pygame.K_UP:
                board.change_direction(c.TOP)
            if event.key == pygame.K_DOWN:
                board.change_direction(c.BOTTOM)
    if i % 20 == 0:
        board.forward()
        if not board.snake.alive:
            print("perdiste!")
            done = True

        # -- Draw everything
        board.draw()

        # Flip screen
        pygame.display.flip()
    i+=1

    # Pause
    clock.tick(60)

pygame.quit()
