class ReutersReadDataSet:
    def __init__(self, filePath):
        self.__aditional_information = {}
        self.__atribute = {}
        self.__data = {}
        self.word=set()
        self.__read_from_File(filePath)
        self.aparition_class={}
        self.__make_aparition_class()
        self.write_gloab_and_s()
        
    def __make_aparition_class(self):
        for i in self.__data:
            for j in self.__data[i]:
                for index in range(0,len(j)-1):
                   self.aparition_class[j[index]] = self.aparition_class.get(j[index], 0) + 1
                   
                   
    def take_aparition_class(self):
        return self.aparition_class

    def __read_from_File(self, filePath):
        with open(filePath, "r") as file:
            for line in file:
                self.__take_aditional_information(line)
                self.__take_atribute(line)
                self.__take_classes(line)

    def __take_aditional_information(self, lines):
        try:
            word = lines.split()
            if word[0][0] == '#':
                self.__aditional_information[word[0][1:]] = int(word[1])
        except:
            pass

    def __take_atribute(self, lines):
        d={}
        try:
            word = lines.split()
            if word[0] == "@attribute":
                d[word[1]] = int(word[2])
                self.__atribute[len(self.__atribute)]=d

                
        except:
            pass


    def __take_classes(self, lines):
        try:
            hash_index = lines.find('#')
            word = lines.split()
            if hash_index != -1 and word[0][1:] not in self.__aditional_information.keys():
                result = lines[hash_index:]
                s = result.split(' ')
                s = [item.replace('\n', '')
                     for item in s if item and item != '#']
                numbers = lines.split('#')[0].split()
                number_pairs = [num.split(':') for num in numbers]
                self.__data[len(self.__data)] = {tuple(s): number_pairs}
        except:
            pass

    def take_aditional_info(self):
        return self.__aditional_information

    def take_atribute(self):
        return self.__atribute

    def take_all_data(self):
        return self.__data

    def take_test(self):
        d = {}
        for key in self.__data:
            for subkey in self.__data[key]:
                if 'Test' in subkey:
                    d[len(d)] = {subkey: self.__data[key][subkey]}
        return d
    def take_train(self):
       d = {}
       for key in self.__data:
           for subkey in self.__data[key]:
               if 'Train' in subkey:
                   d[len(d)] = {subkey: self.__data[key][subkey]}
       return d
   
    def write_gloab_and_s(self):
        with open('output.txt','w') as fs:
            fs.write('Vector global\n')
            fs.write(str(self.__atribute)+'\n')
            fs.write('Vector Rari\n')
            fs.write(str(self.__data)+'\n')