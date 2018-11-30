from Individual import Individual
import random
from Individual import ident

class Population:
    def __init__(self,individuals=[]):
        self.individuals = individuals

    def setRandomPopulation(self,population_size,gen_number,allowed_gens=[0,1],clean_function=ident,mutate_function=ident):
        self.individuals = []
        for index in range(population_size):
            individual = Individual([],clean_function,mutate_function)
            individual.setRandomGens(gen_number,allowed_gens)
            self.individuals.append(individual)

    def setPopulationFromShuffle(self,population_size,toshuffle):
        self.individuals=[]
        for index in range(population_size):
            temp = toshuffle[:]
            random.shuffle(temp)
            self.individuals.append(Individual(temp))


    def copy(self):
        return Population(self.individuals[:])
    def makeSelection(self,fitness,selected_size,tournament_size):
        selected = []
       # print "seleccionando %d individuos, torneos de %d i." % (selected_size,tournament_size)
        for index in range(selected_size):
            best = None
            temp_individuals = self.individuals[:]
            for index2 in range(tournament_size):
                sel_index = random.randint(0,len(temp_individuals)-1)
                individual = temp_individuals.pop(sel_index)
                if best is None or fitness(individual) > fitness(best):
                    best = individual
            selected.append(best)
        self.individuals = selected

    def reproduction(self,N,mutation_rate=0.02,allowed_gens=[0,1]):
        childs = []
        for index in range(N):
            individual1 = self.individuals[random.randint(0,len(self.individuals)-1)]
            individual2 = self.individuals[random.randint(0,len(self.individuals)-1)]
            new_individual = individual1.crossover(individual2)
            new_individual.mutate(mutation_rate,allowed_gens)
            childs.append(new_individual)
        return Population(childs)

    def maxFitness(self,fitness):
        max_fitness = None
        max_fitness_individual = None
        for individual in self.individuals:
            fit_individual = fitness(individual)
            if max_fitness is None or max_fitness<fit_individual:
                max_fitness = fit_individual
                max_fitness_individual = individual
        return (max_fitness,individual)

    def meanFitness(self,fitness):
        mean_fitness = 0
        for individual in self.individuals:
            mean_fitness+=fitness(individual)
        
        return mean_fitness*1.0/len(self.individuals)

    def stdFitness(self,fitness):
        mean = self.meanFitness(fitness)
        std = 0
        for individual in self.individuals:
            std+=(fitness(individual)-mean)**2
        return std*1.0/len(self.individuals)