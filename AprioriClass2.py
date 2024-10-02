from AprioriClass import AprioriL
import pandas as pd


class AprioriC2:
    def __init__(self, path):
        self.L1 = AprioriL(path)
        self.L2 = AprioriL(path)
        self.L3 = AprioriL(path)
        self.df = {}
        self.dictionary={}
        self.keys1 = [i for i in self.L1.df.columns]
        self.keys2 = [i for i in self.L2.df.columns]
        self.keys3 = [i for i in self.L3.df.columns]

    def combine_columns2(self):
        for i in self.keys1:
            for j in self.keys2:
                if i != j:
                    self.df[i+','+j] = self.L1.df[i]
                    self.df[j+','+i] = self.L2.df[j]
        
        self.df=pd.DataFrame(self.df)
        
    def combine_columns3(self):
        for i in self.keys1:
            for j in self.keys2:
                for k in self.keys3:
                  if (i != j)and(i !=k)and(j !=k):
                      self.df[i+','+j+','+k] = self.L1.df[i]
                      self.df[j+','+i+','+k] = self.L2.df[j]
                      self.df[k+','+i+','+j] = self.L3.df[k]
                      
        
        self.df=pd.DataFrame(self.df)


    def count(self):
        for i in range(len(self.df.columns)):
            t = 0
            current_column = self.df.columns[i]
            for index in range(len(self.df) - 1):  # subtract 1 to avoid 'index+1' going out of bounds
                a = self.df.loc[index, current_column]
                b = self.df.loc[index+1, current_column]
                if a != '-' and b != '-':  
                    t = t + 1
        self.dictionary[current_column] = t  # store the count 't' for each column
        print(self.dictionary)

                    # if split_count[0]!=split_count[1] and self.dictionary[split_count[0]+split_count[1]]!='-':
                    #     pass
                    # self.dictionary[split_count[1]+split_count[0]]:
                    #     t++
                    # self.dictionary[split_count[0]+split_count[1]]=v+z
        

    def big_as_prag(self, prag):
        t={}
        for i in self.dictionary:
            if self.dictionary[i]>=prag:
                t[i]=self.dictionary[i]
        print(t)
                
            
            
    def print_count(self):
        print(self.dictionary)
    
    def print_dictionary(self):
        # print(self.df.to_string(header=False,index=False))
        print(self.df)
    
    def make_csv(self):
        self.c2 = self.df
        self.c2.to_csv('output.csv')
