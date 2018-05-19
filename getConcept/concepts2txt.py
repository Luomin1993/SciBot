import nltk
from txt2concept import *


def concepts2txt(concepts_array,path):
    #save the result
	with open(path,'wb') as fW:
         for i in range(len(concepts_array)):
	         fW.write(concepts_array[i])
	         fW.write(' ')

def test_conceepts2txt():
	concepts_array = txt2concepts('./paper_example.txt')
	concepts2txt(concepts_array,'./concepts.txt')




#------------------- TEST -------------
test_conceepts2txt()
