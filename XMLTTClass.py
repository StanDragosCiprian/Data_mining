import json
from XMLReaderClass import XMLReader
#E:\\Facultate\\Data mining\\Reuters\\Reuters_34\\
class XMTT:
    def __init__(self, pathDir):
        self.xml_Training=XMLReader(f"{pathDir}\\Training\\")
        self.xml_Testing=XMLReader(f"{pathDir}\\Testing\\")
        
    def write_file(self):
        with open('out.txt','w') as fs:
            fs.write("Training\n")
            fs.write("Text,title,code:\n")
            index=0
            for i in self.xml_Training.title_and_text:
                fs.write(f"{index}.{i}\n")
                index+=1
            index=0
            for i in self.xml_Training.code_elemts:
                fs.write(f"{index}.{i}\n")
                index+=1
            fs.write("Global Vector:\n")
            json.dump(self.xml_Training.global_words, fs,indent=4)
            fs.write("\nSparse Vector:\n")
            json.dump(self.xml_Training.sparse_vectors, fs,indent=4)
           
            fs.write("\nTesting\n")
            fs.write("Text,title,code:\n")
            index=0
            for i in self.xml_Testing.title_and_text:
                fs.write(f"{index}.{i}\n")
                index+=1
            index=0
            for i in self.xml_Testing.code_elemts:
                fs.write(f"{index}.{i}\n")
                index+=1
            fs.write("Global Vector:\n")
            json.dump(self.xml_Testing.global_words, fs,indent=4)
            fs.write("\nSparse Vector:\n")
            json.dump(self.xml_Testing.sparse_vectors, fs,indent=4)
                
