import pandas as pd


class AprioriL:
    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.item = []
        self.dictionary={}
        self.replace_eliminate()


    def replace_eliminate(self):
        self.df = self.df.replace('?', '-')
        self.df.pop(self.df.columns[0])

    def count_item(self):
        for i in self.df.columns:
            v = self.df[i].value_counts()[i]
            self.dictionary[i]=v
            self.item.append(v)

    def big_as_prag(self, prag):
        print([i for i in self.item if i >= prag])


    def print_prag_dictionary(self,prag):
        t=[i for i in self.df.columns]
        z=[]
        for i in t:
            if self.dictionary[i]>=prag:
                z.append(i)
        print(z)
        
    def print_item(self):
        print(self.item)
        
    def print_item_dictionary(self):
        print(self.dictionary)

    def print_df(self):
        print(self.df.to_string(index=False, header=False))
    
