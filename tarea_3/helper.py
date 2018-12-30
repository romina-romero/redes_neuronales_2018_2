import pygame
from snake_game.Board import Board
from snake_game import constants as c
import matplotlib.pyplot as plt


def simulate(neural_network):
    # Call this function so the Pygame library can initialize itself
    pygame.init()
    board = Board(c.BOX_SIZE)
    board.draw()
    # Set the title of the window
    pygame.display.set_caption('Snake')

    clock = pygame.time.Clock()
    done = False

    i = 0
    while not done:
        if i % 20 == 0:
            if board.snake.alive:
                board.rotate(True)
                ah_food = board.food_distance()
                ah_obs = board.obs_distance()
                board.rotate(False)
                board.rotate(False)
                h_food = board.food_distance()
                h_obs = board.obs_distance()
                board.rotate(True)
                food = board.food_distance()
                obs = board.obs_distance()
                movement = neural_network.feed([food, obs, ah_food, ah_obs, h_food, h_obs])
                if movement[1] > movement[0] and movement[1] > movement[2]:
                    board.rotate(True)
                elif movement[2] > movement[0] and movement[2] > movement[1]:
                    board.rotate(False)
                board.forward()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # -- Draw everything
        board.draw()

        # Flip screen
        pygame.display.flip()
        i += 1

        # Pause
        clock.tick(60)

    pygame.quit()


def plot_all(maxs, means, stds):
    xs = range(len(maxs))
    plt.ylim(bottom=0, top=max(maxs))
    plt.subplots_adjust(hspace=1)
    plt.subplot(311)
    plt.plot(xs, maxs)
    plt.title('Maximos alcanzados por generacion')
    plt.subplot(312)
    plt.plot(xs, means)
    plt.title('Promedios por generacion')
    plt.subplot(313)
    plt.plot(xs, stds)
    plt.title('Desviacion estandard por generacion')
    plt.show()
