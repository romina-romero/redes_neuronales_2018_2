import matplotlib.pyplot as plt
from scipy.spatial import distance
import random

def get_datasets():
    counter = 0
    train_set = []
    test_set = []
    train_labels=[]
    test_labels=[]

    positive=[]
    negative=[]
    for line in open('../spambase/spambase.data'):
        values = map(float,line.strip().replace('\n','').replace('\r','').split(','))
        if values[-1]==1:
            positive.append(values)
        else:
            negative.append(values)
    print "Extraidos %d positivos y %d negativos" % (len(positive),len(negative))
    for index in range(len(positive)):
        if index <= len(positive)/2:
            train_set.append(positive[index][:-1])
            train_labels.append([positive[index][-1]])
        else:
            test_set.append(positive[index][:-1])
            test_labels.append([positive[index][-1]])
    for index in range(len(negative)):
        if index <= len(negative)/2:
            train_set.append(negative[index][:-1])
            train_labels.append([negative[index][-1]])
        else:
            test_set.append(negative[index][:-1])
            test_labels.append([negative[index][-1]])
        #if counter < 2601:
        #    train_set.append(values[:-1])
        #    train_labels.append([values[-1]])
        #else:
        #    test_set.append(values[:-1])
        #    test_labels.append([values[-1]])
        #counter+=1
    return (train_set,train_labels,test_set,test_labels)
def shuffle_dataset(dataset,labels):
    for_shuffle = []
    for index in range(len(dataset)):
        for_shuffle.append([labels[index],dataset[index]])
    random.shuffle(for_shuffle)
    shuffle_dataset = []
    shuffle_labels = []
    for index in range(len(dataset)):
        shuffle_dataset.append(for_shuffle[index][1])
        shuffle_labels.append(for_shuffle[index][0])
    return (shuffle_dataset,shuffle_labels)

def plot_error(x,y,title):
    plt.ylim(bottom=0,top=max(y))
    plt.plot(x,y)
    plt.title(title)
    plt.xlabel("Cantidad")
    plt.ylabel("Error cuadratico")
    plt.show()

def plot_prec(x,y,title):
    plt.ylim(bottom=0,top=max(y))
    plt.plot(x,y)
    plt.title(title)
    plt.xlabel("Cantidad")
    plt.ylabel("Precision")
    plt.show()


def test_network(network,test_set,outputs):
    corrects = 0
    for index in range(len(test_set)):
        result = network.feed(test_set[index])
        dist = distance.euclidean(result,outputs[index])
        if dist<=0.5:
            corrects+=1
    return (corrects*1.0/len(test_set),dist**2)

    