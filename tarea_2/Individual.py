import random

def ident(gens):
    return gens

class Individual:

    def __init__(self,gens=[],clean_function=ident,mutate_function = ident):
        self.gens = gens
        self.clean_function = clean_function
        self.mutate_function = mutate_function
        self.clean_function(self.gens)


    def setRandomGens(self,gen_number,allowed_gens=[0,1]):
        self.gens = []
        for index in range(gen_number):
            self.gens.append(random.choice(allowed_gens))
        self.clean_function(self.gens)

    def crossover(self,individual_2):
        mixing_point = random.randint(1,len(self.gens)-1)
        new_comb = self.gens[:mixing_point]+individual_2.gens[mixing_point:]
        self.mutate_function(new_comb)
        return Individual(new_comb)

    def mutate(self,mutation_rate=0.02,allowed_gens=[0,1]):
        number_gens_mutated = int(round(len(self.gens)*mutation_rate))
        for index in range(number_gens_mutated):
            self.gens[random.randint(0,len(self.gens)-1)] = random.choice(allowed_gens)

    def mutateWithFunction(self,mutator):
        mutator(self.gens)