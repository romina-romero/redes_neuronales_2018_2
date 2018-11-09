import time
import sys
sys.path.append('../trabajo_incremental')
from NeuralNetwork import NeuralNetwork
import test_helper



def main():
    (train_set,train_labels,test_set,test_labels) = test_helper.get_datasets()
    lrs = [0.1,0.5,1.0,1.5]
    n = NeuralNetwork()
    t_init = time.time()
    for lr in lrs:
        n.make(57,[38,1],lr)
        print "Prueba con lr=%.1f" % (lr)
        precisions = []
        sizes = []
        errors = []
        for index in range(len(train_set)):
            n.train(train_set[index],train_labels[index])
            if (index+1)%10 ==0:
                print "Entrenado con %d de %d, a %d segundos de inicio" % (index+1,len(train_set),time.time()-t_init)
                (precision,error) = test_helper.test_network(n,test_set,test_labels)
                precisions.append(precision)
                errors.append(error) 
                sizes.append(index+1)
        test_helper.plot_error(sizes,errors,"Error con lr=%.1f" % (lr))
        test_helper.plot_prec(sizes,precisions,"Precision con lr=%.1f" % (lr))
        
if __name__ == '__main__':
    main()