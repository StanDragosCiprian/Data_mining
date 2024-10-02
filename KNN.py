from ReutersDataSet import ReutersReadDataSet
from Trasaturi import TrasaturiClass
from collections import Counter
import numpy as np
from TD import TopicsDictionary
import math
class KNNClass:
    def __init__(self,prag,k=3):
        self.__reuters = TrasaturiClass("E:\\Facultate\\Data mining\\ReutersDataSet-arff\\AllReutersData34.arff")
        self.test=self.get_topics(prag,"Test")
        self.traing=self.get_topics(prag,"Train")
        self.k=k
        
    def get_topics(self,prag,t):
        list=[]
        r=self.__reuters.take_vec(prag,t)
        for key,val in r.items():
            for i in range(0,len(key)-1):
                list.append(TopicsDictionary(key[i],val))
        return list
   
    def manhattan_distance(self,vec1, vec2):
        return sum(abs(float(x) - float(y)) for x, y in zip(vec1, vec2))
    def similarity_distance(self,vec1, vec2):
        return math.sqrt(sum((float(x) - float(y))**2 for x, y in zip(vec1, vec2)))
    
    def normalize_sum1(self, vec):
        sum_val = sum(vec)
        return [float(i)/sum_val for i in vec]

    def normalize(self, vec):
        min_val = min(vec)
        max_val = max(vec)
        return [(float(i)-min_val) / (max_val-min_val) for i in vec]

    def k_algorithm(self, normalization_func,distant_func):
        distances=[]
        for i in self.test:
            test_vec=normalization_func(i.get_vector())
            for k in self.traing:
                train_vec=normalization_func(k.get_vector())
                distance=distant_func(test_vec,train_vec)
                distances.append([distance,k.get_topic()])
        distances.sort()
        neighbors = distances[:self.k]
        votes = Counter(topic for _, topic in neighbors)
        prediction, _ = votes.most_common(1)[0]
        print(prediction)

