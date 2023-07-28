from torchvision import datasets
import numpy as np

class Cifar10Dataset(datasets.CIFAR10):
    
    def __init__(self, root='./data', download=True):
       super(Cifar10Dataset, self).__init__(root=root, )