from Population import Population
from Individual import ident
import matplotlib.pyplot as plt
import time
def display(individual):
    print individual.gens

class Tester:
    def __init__(self,fitnessFunction,alphabeth=[0,1],genSize=128,populationSize=100,threshold=0,cleanFunction=ident,mutateFunction=ident,visualizationFunction=display):
        self.fitnessFunction = fitnessFunction
        self.alphabeth = alphabeth
        self.genSize = genSize
        self.populationSize = populationSize
        self.threshold=threshold
        self.cleanFunction=cleanFunction
        self.mutateFunction=mutateFunction
        self.visualizationFunction=visualizationFunction

    def test(self):
        population = Population()
        population.setRandomPopulation(self.populationSize,self.genSize,self.alphabeth,self.cleanFunction,self.mutateFunction)
        (max_fit,best_individual) = population.maxFitness(self.fitnessFunction)
        mean_fit = population.meanFitness(self.fitnessFunction)
        std_fit = population.stdFitness(self.fitnessFunction)

        print "max: %.2f, mean: %.2f, std: %.2f" % (max_fit,mean_fit,std_fit) 

        generations = 0
        t_ini = time.time()

        maxs = [max_fit]
        means = [mean_fit]
        stds = [std_fit]

        last_improvement=0

        while max_fit<self.threshold:

            population.makeSelection(self.fitnessFunction,int(round(self.populationSize/4.0)),int(round(self.populationSize/2.0)))
            population = population.reproduction(self.populationSize,0.02,self.alphabeth)
            generations+=1
            (max_fit_2,best_individual_2) = population.maxFitness(self.fitnessFunction)

            if max_fit_2<=max_fit:
                last_improvement+=1
                if last_improvement>=50:
                    print "Solucion no encontrada: 50 generaciones estancadas"
                    break
            else:
                last_improvement=0
                max_fit = max_fit_2
                best_individual = best_individual_2

            mean_fit = population.meanFitness(self.fitnessFunction)
            std_fit = population.stdFitness(self.fitnessFunction)

            maxs.append(max_fit)
            means.append(mean_fit)
            stds.append(std_fit)

            print "max: %.2f, mean: %.2f, std: %.2f" % (max_fit,mean_fit,std_fit)
            
           # raw_input()
        t_total = time.time()-t_ini
        print "Pasadas %d generaciones, en %.2f segundo(s)" % (generations,t_total)
        self.plot_all(maxs,means,stds)
        print "Mejor solucion"
        self.visualizationFunction(best_individual)

    def plot_all(self,maxs,means,stds):
        xs = range(len(maxs))
        plt.ylim(bottom=0,top=max(maxs))
        plt.subplots_adjust( hspace=1)
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