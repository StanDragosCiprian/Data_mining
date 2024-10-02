from ReutersDataSet import ReutersReadDataSet

import math

class TrasaturiClass:
    def __init__(self, path):
        self.__reuters = ReutersReadDataSet(path)
        self.test=self.__reuters.take_test()
        self.train=self.__reuters.take_train()
        self.all_data=self.__reuters.take_all_data()
        self.total_number=len(self.train)+len(self.test)
        self.aparition_class=self.__reuters.take_aparition_class()
        self.index=[]
        self.global_vector={}
        self.atribute=self.__reuters.take_atribute()
        # self.in_win_test=self.__informational_wining(self.test,len(self.test))
        # self.in_win_train=self.__informational_wining(self.train,len(self.train))
        self.in_win_all_data=self.__informational_wining(self.all_data,len(self.all_data),self.all_data)
        
    def take_word(self,doc):
        result = []
        for key in doc:
            if isinstance(doc[key], dict):
                for sub_key in doc[key]:
                    result.extend(doc[key][sub_key])
            else:
                result.extend(doc[key])
        return result
    def __informational_wining(self,v,total_doc,doc):
       E2_list= self.make_E2(v)
       E3_list= self.make_E3(v,total_doc)
       informational_win=[]
       count_item=self.count_items(v)

       word_list=self.take_word(v)
       words=[int(i[0]) for i in word_list]
       words=set(words)
    #    
       general_entropy=self.take_general_entropy(v,total_doc)
       for i in words:
            f1=(count_item[str(i)]/total_doc)
            f2=((total_doc-count_item[str(i)])/(total_doc))
            
            E2=E2_list[int(i)]
            E3=E3_list[int(i)]
            pinf=(general_entropy)-(f1*E2)-(f2*E3)
            informational_win.append(pinf)
       return informational_win

    #    return self.take_general_entropy(v,total_doc)-self.make_E2(v)-self.make_E3(v,total_doc)
    def take_aditional_info(self):
        return self.__reuters.take_aditional_info()
    def __take_just_word(self,d):
        result = []
        for key in d:
            if isinstance(d[key], dict):
                for sub_key in d[key]:
                    result.extend(d[key][sub_key])
            else:
                result.extend(d[key])
        return result
    def take_general_entropy(self,c,total_number):
        entropy=0
        c=self.__make_aparition_class(c)
        for ap in c:
            p=int(c[ap])/total_number
            entropy+=p*math.log2(p)
            entropy=-entropy
        return entropy
   
    def count_items(self, doc):
      counts = {}
      for key, value in doc.items():
          for subkey, subvalue in value.items():
              for item in subvalue:
                  item_key = item[0]
                  if item_key not in counts:
                      counts[item_key] = 0
                  counts[item_key] += 1
      return counts
    def make_E2(self,doc):
        word_apparition_in_class=self.word_apparition_in_class(doc)
        E2={}
        count_item=self.count_items(doc)
        for class_word in word_apparition_in_class:
            for word in word_apparition_in_class[class_word]:
                index=word_apparition_in_class[class_word][word]
                w=word
                p=index/count_item[w]
                calc=(p)*math.log2(p)
                if int(w) in E2:
                    E2[int(w)]-=calc
                else:
                    E2[int(w)]=calc 
        return E2
        
    def word_apparition_in_class(self, doc):
        c = {}
        for key, value in doc.items():
            for subkey, subvalue in value.items():
                for i in range(0,len(subkey)-1):
                    if subkey[i] not in c:
                        c[subkey[i]] = {}
                    for item in subvalue:
                        item_key = item[0]
                        if item_key not in c[subkey[i]]:
                            c[subkey[i]][item_key] = 0
                        c[subkey[i]][item_key] += 1
        return c
                            
    def make_E3(self, doc,l):
        word_apparition_in_class=self.word_apparition_in_class(doc)
        E3={}
        count_item=self.count_items(doc)

        for class_word in word_apparition_in_class:
            for word in word_apparition_in_class[class_word]:
                index=word_apparition_in_class[class_word][word]
                w=word
                p=(index)/(l-count_item[w])
                if p !=0:
                    calc=(p)*math.log2(p)
                if int(w) in E3:
                    E3[int(w)]-=calc
                else:
                    E3[int(w)]=calc
        return E3
   
    def __make_aparition_class(self,data):
        dict={}
        for i in data:
            for j in data[i]:
                for index in range(0,len(j)-1):
                   dict[j[index]] = dict.get(j[index], 0) + 1
        return dict
                   
    def take_atribute(self):
        return self.global_vector

    def take_all_data(self):
        return self.__reuters.take_all_data()
    
    def spate_vect(self,doc,index):
        s={}
        
        for i in doc:
            for key,value in doc[i].items():
                l=[]
                for z in value:
                    for indexes in index:
                        if int(z[0])==indexes:
                            l.append(z)
                s[key]=l
        return s
    def iterate_with_prag(self,prag,doc_win,doc):
        self.index.clear
        self.atribute.clear
        gv={}
        g={}
        z=doc
        count=0
        for i in doc_win:
            if len(self.atribute)!=0:
                if i >=prag:
                   self.index.append(count)
                   k=list(self.atribute[count].keys())[0]
                   gv[k]=i
                   
                   print(k,":",i)

                count+=1
            else:
                print(i)
        self.global_vector=gv
        f=self.spate_vect(doc,self.index)
        for key,value in f.items():
            if value!=[]:
                print(key,":",value)
                g[key]=value
                
        pass
    def take_vec(self,prag,t):
        self.index.clear

        count=0
        for i in self.in_win_all_data:
            if len(self.atribute)!=0:
                if i >=prag:
                   self.index.append(count)
                   k=list(self.atribute[count].keys())[0]
                count+=1
            else:
                print(i)
        
        f=self.spate_vect(self.all_data,self.index)
        g={}
        for key,value in f.items():
            if value!=[]:
                if key[len(key)-1]==t:
                    g[key]=value
        
            
        return g
    def doc_vector(self,doc_type):
        
        pass
        
    def get_wining_data(self):
        return self.in_win_all_data
    def print_value(self,prag):
        # print(f"Test\n")
        # self.iterate_with_prag(prag,self.in_win_test)
        # print(f"Train\n")
        # self.iterate_with_prag(prag,self.in_win_train)
        print(f"All data\n")
        self.iterate_with_prag(prag,self.in_win_all_data,self.all_data)