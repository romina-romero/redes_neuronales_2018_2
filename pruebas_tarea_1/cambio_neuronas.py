import time
import sys
sys.path.append('../trabajo_incremental')
from NeuralNetwork import NeuralNetwork
import test_helper


def main():
    (train_set,train_labels,test_set,test_labels) = test_helper.get_datasets()
    n = NeuralNetwork()
    t_init = time.time()
    n.make(57,[38,1])
    n2 = n.copy()
    for index in range(len(train_set)):
        n.train(train_set[index],train_labels[index])
    diff = n.diff(n2)
    diff.print_arch()
if __name__ == '__main__':
    main()