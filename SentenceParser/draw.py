import os
from nltk.parse import stanford

#添加stanford环境变量,此处需要手动修改，jar包地址为绝对地址。
os.environ['STANFORD_PARSER'] = './jars/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = './jars/stanford-parser-3.5.0-models.jar'


#为JAVAHOME添加环境变量
java_path = "C:/Program Files (x86)/Java/jdk1.8.0_11/bin/java.exe"
os.environ['JAVAHOME'] = java_path

#句法标注
parser = stanford.StanfordParser(model_path="./stanford-parser-full-2014-10-31/stanford-parser-3.5.0-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
sentences = parser.parse_sents("Hello, My name is Melroy.".split(), "What is your name?".split())
print sentences

# GUI
for sentence in sentences:
    sentence.draw()
