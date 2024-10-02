import xml.etree.ElementTree as ET
import os
import re
from nltk.stem import PorterStemmer


class XMLReader:
    def __init__(self, pathDir):
        self.__files = os.listdir(pathDir)
        self.xmls = self.__generate_xml(pathDir)
        self.global_words = {}
        self.stemmer = PorterStemmer()
        self.__titles = [
            re.sub('[^a-zA-Z ]', '', i.find('title').text) for i in self.xmls if i.find('title') is not None
        ]
        self.__text = [''.join([re.sub(r'[^a-zA-ZeE ]', '', p.text) for p in i.find(".//text").iter("p")]) for i in self.xmls]
        self.code_elemts = [[code.attrib["code"] for code in i.find(".//codes[@class='bip:topics:1.0']").findall(".//code")] for i in self.xmls]
        self.title_and_text=[self.__titles[i]+" "+self.__text[i] for i in range(0,len(self.__titles))]
        self.__fill_global_with_title()
        self.sparse_vectors = {i: {self.stemmer.stem(word): text.count(word) for word in text.split() if not self.__is_stop_word(self.stemmer.stem(word))} for i, text in enumerate(self.title_and_text)}
        
    
    def __generate_xml(self, path):
        r = []
        for i in self.__files:
            with open(f"{path}{i}", 'rt') as f:
                et = ET.parse(f)
                root = et.getroot()
                r.append(root)
        return r
    
    
    def __is_stop_word(self,word):
        stop_words = [line.strip() for line in open("E:\\Facultate\\Data mining\\stopwords.txt","r")]
        return word.lower() in stop_words 

    def __fill_global_with_title(self):
        for title_and_text_list in self.title_and_text:
            index=0
            tt=title_and_text_list.split()
            for word in tt:
                stemmed_word = self.stemmer.stem(word)
                if stemmed_word not in self.global_words:
                    self.global_words[stemmed_word] = index
                index += 1
      

    def write_file(self):
        with open("output.txt", "w") as file1:
            file1.write("Global vector \n")
            for word in self.global_words:
                file1.write(word + "\n")
            
            file1.write("\nSparse vector\n")
            for index, word_dict in self.sparse_vectors.items():
                file1.write(str(index) + ": " + str(word_dict) + "\n")



