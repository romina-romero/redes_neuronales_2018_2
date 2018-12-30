from neural_network.NeuralNetwork import NeuralNetwork
import random
from .Individual import Individual


class Population:

    def __init__(self, individuals=None):
        self.individuals = individuals
        if individuals is None:
            self.individuals = []

    def make_population(self, population_size, input_size, layer_sizes, lr=0.5):
        self.individuals = []
        for i in range(population_size):
            network = NeuralNetwork()
            network.make(input_size, layer_sizes, lr)
            self.individuals.append(Individual(network))

    def make_selection(self, fitness, selected_size):
        '''  selected = []
        for index in range(selected_size):
            best = None
            temp_individuals = self.individuals[:]
            for index2 in range(tournament_size):
                sel_index = random.randint(0, len(temp_individuals) - 1)
                individual = temp_individuals.pop(sel_index)
                if best is None or fitness(individual) > fitness(best):
                    best = individual
            selected.append(best)
        self.individuals = selected
        '''
        sorted_pop = []
        selected = []
        for index in range(len(self.individuals)):
            sorted_pop.append([fitness(self.individuals[index]), index])
        sorted_pop.sort(reverse=True)
        for i in range(selected_size):
            selected.append(self.individuals[sorted_pop[i][1]])
        self.individuals = selected

    def reproduction(self, population_size, fitness, mutation_rate=0.02, elite=0):
        childs = []
        for index in range(population_size):
            if index < elite:
                childs.append(self.individuals[index])
                continue
            individual1 = self.individuals[random.randint(0, len(self.individuals) - 1)]
            individual2 = self.individuals[random.randint(0, len(self.individuals) - 1)]
            new_individual = individual1.crossover(individual2, fitness)
            childs.append(new_individual)

        number_of_mutations = int(round(population_size*mutation_rate))
        indexes = list(range(population_size))
        random.shuffle(indexes)
        for index in range(number_of_mutations):
            index_mutate = indexes.pop()
            to_mutate = childs[index_mutate]
            to_mutate.mutate()
        return Population(childs)

    def max_fitness(self, fitness):
        max_fitness = None
        max_fitness_individual = None
        for individual in self.individuals:
            fit_individual = fitness(individual)
            if max_fitness is None or max_fitness < fit_individual:
                max_fitness = fit_individual
                max_fitness_individual = individual
        return max_fitness, max_fitness_individual

    def mean_fitness(self, fitness):
        mean_fitness = 0
        for individual in self.individuals:
            mean_fitness += fitness(individual)

        return mean_fitness * 1.0 / len(self.individuals)

    def std_fitness(self, fitness):
        mean = self.mean_fitness(fitness)
        std = 0
        for individual in self.individuals:
            std += (fitness(individual) - mean) ** 2
        return std * 1.0 / len(self.individuals)

