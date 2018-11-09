import time
import sys
sys.path.append('../trabajo_incremental')
from NeuralNetwork import NeuralNetwork
import test_helper

def test(n,capas):
    (train_set,train_labels,test_set,test_labels) = test_helper.get_datasets()
    (shuffle_set,shuffle_label) = test_helper.shuffle_dataset(train_set,train_labels)

    t_init = time.time()
    #n.make(57,[38,1])
    precisions = []
    sizes = []
    errors = []
    for index in range(len(train_set)):
        n.train(shuffle_set[index],shuffle_label[index])
        if (index+1)%10 ==0:
            print "Entrenado con %d de %d, a %d segundos de inicio" % (index+1,len(train_set),time.time()-t_init)
            (precision,error) = test_helper.test_network(n,test_set,test_labels)
            precisions.append(precision)
            errors.append(error) 
            sizes.append(index+1)
    s = ""
    print "Tiempo total: %d segundos" % (time.time()-t_init)
    if capas>1:
        s="s"
    test_helper.plot_error(sizes,errors,"Error con %d capa%s oculta%s" % (capas,s,s))
    test_helper.plot_prec(sizes,precisions,"Precision con %d capa%s oculta%s" % (capas,s,s))


def main():
    n = NeuralNetwork()
    #con una capa oculta
    print "Prueba una capa oculta"
    n.make(57,[38,1])
    test(n,1)
    #con dos capas
    print "Prueba dos capas ocultas"
    n.make(57,[38,38,1])
    test(n,2)
    #con tres capas
    print "Prueba tres capas ocultas"
    n.make(57,[38,38,38,1])
    test(n,3)

if __name__ == '__main__':
    main()