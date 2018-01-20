import nltk
import sys
import os

#data is in /root/nltk
#nltk.download('punkt')
methods = ['minimize','optimization','genetic_optimization']
formats = ['models_1D','models_3D','objective_function','TRACK']
#sentence = 'In fact,I wanna use genetic optimization on the models 3D;'
sentence = sys.argv[1]
words = nltk.word_tokenize(sentence)
word_tag = nltk.pos_tag(words)
for me in methods:
	for fo in formats:
		if (me.replace('_',' ') in sentence) and (fo.replace('_',' ') in sentence):
		   os.system('./exe ' + me + ' ' + fo )