import nltk

readin_tags = ['NN','RB','JJ']
end_tags    = ['NN']


def getLine(path):
    f     = open(path)  
    lines = f.readlines()
    return lines

def test_getLine():
    print getLine('./paper_example.txt')    

def getConcept(string):
    if string == '':
       return []
    text     = nltk.word_tokenize(string)
    tags     = nltk.pos_tag(text)
    concepts = []
    concept  = ''
    i        = 0
    for tag in tags:
        if tag[1] in readin_tags:
           concept = concept + ' ' +tag[0]  
        #elif concept!='' and (tags[i-1][1] in end_tags):
        elif (tags[i-1][1] in end_tags) and concept.count(' ')>1:
           #print nltk.pos_tag(nltk.word_tokenize(concept[-1]))
           concepts.append(concept)
           concept = ''
        else:
           concept = ''   
        i+=1   
    return concepts

def test_getConcept():
    string = 'Im busy,Optimizations using predefined rates,For a computer model online for large scale parallel particle tracking codes with space'
    print getConcept(string)

def txt2concepts(path):
    txt = getLine(path)
    concepts = []
    for line in txt:
        #print line.replace('\n','')
        concepts = concepts + getConcept(line.replace('\n',''))
    return concepts

def test_txt2concepts():
    print txt2concepts('./paper_example.txt')        


if __name__ == '__main__':
    #test_getConcept()
    #test_getLine()
    test_txt2concepts()