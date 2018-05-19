import nltk

sentence = "Active people often send the friend-circle photos because of small things."
s_1      = "Active people often send the friend-circle photos because of small things."
s_2      = "Lv is an active man in the friend-circle."
#s_3      = "He will send friend-circle photos on marrige of SunYiKai."
s_3 = "we will implement deep learning algorithms with very simple codes"
tokens   = nltk.word_tokenize(sentence)
tags     = nltk.pos_tag(tokens)
ss       = [s_1,s_2,s_3]
for sen in ss:
    tk = nltk.word_tokenize(sen)
    tg = nltk.pos_tag(tk)
    print ' '
    print tg

#print tags
