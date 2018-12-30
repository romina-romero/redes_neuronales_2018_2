from neuroevolution.Population import Population
from snake_game.Board import Board
import snake_game.constants as c
from helper import simulate, plot_all
import time

POPULATION_SIZE = 100
GENERATIONS = 1000
SELECTION_SIZE = 20
MUTATION_RATE = 0.3
ELITE = 5

def fitness(individual):
    board = Board(c.BOX_SIZE, False)
    i=0
    prev_size = 2
    while board.snake.alive:
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
        movement = individual.neural_network.feed([food, obs, ah_food, ah_obs, h_food, h_obs])
        if movement[0] > movement[1] and movement[0] > movement[2]:
            board.forward()
        elif movement[1] > movement[0] and movement[1] > movement[2]:
            board.rotate(True)
            board.forward()
        else:
            board.rotate(False)
            board.forward()
        if len(board.snake.segments) > prev_size:
            prev_size = len(board.snake.segments)
            i = 0
        i+=1
        if i%225 == 0:
            break
    return len(board.snake.segments) + i/225.0

def main():

    population = Population()
    #inputs:1: distancia comida sin moverme
    #       2: distancia obstaculo sin moverme
    #       3: distancia comida girar antihorario
    #       4: distancia obs girar antihorario
    #       5: distancia comida girar horario
    #       6: distancia obs girar horario
    #outputs:   1: quedarme
    #           2: giro antihorario
    #           3: giro horario
    population.make_population(POPULATION_SIZE, 6, [10, 3])

    (absolute_max, absolute_max_ind) = population.max_fitness(fitness)
    fmean = population.mean_fitness(fitness)
    fstd = population.std_fitness(fitness)
    maxs = [absolute_max]
    means = [fmean]
    stds = [fstd]

    print("fitnes maximo: %.3f, promedio: %.3f, std: %.3f" % (absolute_max,
                                                              fmean,
                                                              fstd))
    number_or_generations = 1
    t_ini = time.time()
    while number_or_generations<GENERATIONS:
        population.make_selection(fitness, SELECTION_SIZE)
        population.reproduction(POPULATION_SIZE, fitness, MUTATION_RATE, ELITE)
        (maxf, best_ind) = population.max_fitness(fitness)
        if maxf > absolute_max:
            absolute_max = maxf
            absolute_max_ind = best_ind
        meanf = population.mean_fitness(fitness)
        stdf = population.std_fitness(fitness)

        maxs.append(maxf)
        means.append(meanf)
        stds.append(stdf)
        print("fitnes maximo: %.3f, promedio: %.3f, std: %.3f, gen=%d, max_absoluto: %.3f, tiempo ejecucion: %d" % (maxf,
                                                                                              meanf,
                                                                                              stdf,
                                                                                              number_or_generations,
                                                                                              absolute_max,
                                                                                              time.time() - t_ini))
        number_or_generations+=1
    t_fin = time.time() - t_ini
    print("Pasadas %d generaciones, en %.2f segundo(s)" % (GENERATIONS, t_fin))
    simulate(absolute_max_ind.neural_network)
    plot_all(maxs, means, stds)

if __name__=='__main__':
    main()