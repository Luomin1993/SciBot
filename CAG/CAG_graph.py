#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import re
import csv
import sys
import nltk

class Event(object):
    """docstring for Event"""
    params = [];
    Subject='';Object='';
    text = '';
    Type = 'Event';
    def __init__(self, params):
        super(Event, self).__init__()
        self.params = params
        for param in params:
            self.text += " "+param.text;

class State(object):
    """docstring for State"""
    def __init__(self, arg):
        super(State, self).__init__()
        self.arg = arg
        
        


class GraphNode(object):
    """Node in CAG"""
    Type = "";
    text = "";
    Linked_Nodes = []; #其中的元素为turple:(Node类型,edge类型);
    #def __init__(self, arg):
    #    super(GraphNode, self).__init__();
    #    self.arg = arg;

    def __init__(self,Type,text):
        # if Type == "Event":
        #     self.text = "Event";
        #     self.Type = "Event";
        #     return 0;
        # if Type == "State":
        #     self.text = "State";
        #     self.Type = "State";
        #     return 0;
        self.Type = Type;
        self.text = text;

    #def __init__(self,Type,Event):
    #    if Type == "Event":
    #        self.text = "Event";
    #        self.Type = "Event";
    #    if Type == "State":
    #        self.text = "State";
    #        self.Type = "State";
            

    def link(self,another_node):
        Linked_Nodes.append((another_node,self.Edge_Type(another_node)));    

    def Edge_Type(self,another_node):
        return self.Type + "__" + another_node.Type;

Event_Vwords_tags_set = ['VBP','RB','VB','MD'];
State_Vwords_tags_set = ['RB','VBZ','MD'];
Union_Vwords_tags_set = [];
RB_Vwords_tags_set = [];

Con_tags_set = ['JJ','NN','NNS','NNP','DT','PRP','VBG'];
In_tags_set  = ['IN'];

Line_Dict = {'Con_VBP':'--->','Con_VB':'--->','Con_MD':'--->','MD_VB':'-->','VB_Con':'--->','VBP_Con':'--->','Con_In':'===','In_Con':'==='};

class CAG(object):
    """docstring for CAG"""
    sentence   = "";
    CAG_tokens = [];
    CAG_Nodes  = [];
    CAG_Graph  = [];
    def __init__(self):
        super(CAG, self).__init__();

    def read_sentence(self,sentence):
        self.sentence   = sentence;
        tokens          = nltk.pos_tag(nltk.word_tokenize(sentence));
        self.CAG_tokenize(tokens);
        self.link_all();     

    def link_two(self,node1,node2):
        node1.link(node2);
        node2.link(node1);

    def CAG_tokenize(self,tokens):
        CAG_token = ["",""];
        index     = 0;
        for token in tokens:
            # if token[1] in In_tags_set:  #如果是一个副词
            #     if CAG_token[0]!="" and CAG_token[1]=="In": #承上：上一个词也是是副词
            #         if tokens[index+1][1] in In_tags_set:CAG_token[0] += " "+token[0];index +=1;continue; #启下：如果下一个也是副词
            #         else:self.CAG_tokens.append(CAG_token);CAG_token = ["",""];index +=1;continue;#启下：下一个不是副词，此乃最后一个;
            #     else: CAG_token[0] += token[0];CAG_token[1]="In";index +=1;continue; #承上：上一个不是副词；  
                      
            if token[1] in In_tags_set: #如果是介词
                if CAG_token[0]!="" and CAG_token[1]=="In": #承上：上一个词也是介词
                    if index<len(tokens)-1 and tokens[index+1][1] in In_tags_set:CAG_token[0] += " "+token[0];index +=1;continue; #启下：如果下一个也是介词
                    else:CAG_token[0] += " "+token[0];self.CAG_tokens.append(CAG_token);CAG_token = ["",""];index +=1;continue; #启下：如果下一个不是介词，此乃最后一个
                else:  #承上：上一个词不是介词
                    if index<len(tokens)-1 and tokens[index+1][1] in In_tags_set:CAG_token[0]=token[0];CAG_token[1]="In";index +=1;continue; #启下：如果下一个也是介词
                    else:CAG_token[0]=token[0];CAG_token[1]="In";self.CAG_tokens.append(CAG_token);CAG_token = ["",""];index +=1;continue; #启下：如果下一个也不是介词，此乃一个

            if token[1] in Con_tags_set: #如果是概念词
                if CAG_token[0]!="" and CAG_token[1]=="Con": #承上：上一个词也是概念词
                    if index<len(tokens)-1 and tokens[index+1][1] in Con_tags_set:CAG_token[0] += " "+token[0];index +=1;continue; #启下：如果下一个也是概念词
                    else:CAG_token[0] += " "+token[0];self.CAG_tokens.append(CAG_token);CAG_token = ["",""];index +=1;continue; #启下：如果下一个不是概念词，此乃最后一个
                else:  #承上：上一个词不是概念词
                    if index<len(tokens)-1 and tokens[index+1][1] in Con_tags_set:CAG_token[0]=token[0];CAG_token[1]="Con";index +=1;continue; #启下：如果下一个也是概念词
                    else:CAG_token[0]=token[0];CAG_token[1]="Con";self.CAG_tokens.append(CAG_token);CAG_token = ["",""];index +=1;continue; #启下：如果下一个也不是概念词，此乃一个
            if token[1] == 'RB': #'very simple code'
                if tokens[index+1][1] in Con_tags_set:CAG_token[0]=token[0];CAG_token[1]="Con";index +=1;continue; #启下：如果下一个是概念词       
                    
            self.CAG_tokens.append([token[0],token[1]]);
            index +=1;            
        
    def link_all(self):
        if self.sentence == "":
            return 0;
        for token in self.CAG_tokens:
            self.CAG_Nodes.append(GraphNode(token[1],token[0]));
        Temp_parser = [];
        index       = 0;
        #找Event的基本思路是，默认整个CAG_Nodes的分布是[Con1,...,Con2,...,Con3,... ...]
        #那么每捕捉一个Temp_parser=[Con1,...,Con2](即两头是Con类型的节点)就判断是否符合Event/State;
        #不符合就调整Temp_parser=[Con2]然后继续遍历.
        #所以一遍遍历就专注找Event/State,不做其他事。最终可以用O(n)的时间复杂度解决。

        #这一步遍历只负责找Event/State;
        for Node in reversed(self.CAG_Nodes): #逆序遍历才能解决"I think you should work harder!"
            #if len(Temp_parser)>2 and Temp_parser[-1].Type=="Con" and Temp_parser[0].Type=="Con"
            if Node.Type == "Con": #当前节点是"Con"
                Temp_parser.append(Node); #先将当前节点添加进去           
                if len(Temp_parser)>2 and Temp_parser[0].Type=="Con": #已经达到判断条件Temp_parser=[Con1,...,Con2]
                    if self.fitEvent(Temp_parser): #判断是否符合Event结构
                       #print "We are Here"
                       self.CAG_Graph.append(Event(Temp_parser)); #构造Event节点并加入到CAG_Graph;
                       Temp_parser = []; #清空Temp_parser
                       continue;
                    elif self.fitState(Temp_parser): #判断是否符合State结构
                       self.CAG_Graph.append(State(Temp_parser)); #构造State节点并加入到CAG_Graph;
                       Temp_parser = []; #清空Temp_parser
                       continue;
                    else: # 不是Event/State结构，可能是[Con1,In,Con2]这种
                       self.CAG_Graph += Temp_parser[0:-1]; #注意这一步，Temp_parser里的东西除了最后加入的Con都不是Event/State一部分,所以先加入到CAG_Graph里
                       Temp_parser = [Temp_parser[-1]]; #只保留最后一个Con然后继续遍历;  
                       continue;
                #else:
                #    Temp_parser.append(Node);  
            else: #当前节点不是"Con"
                Temp_parser.append(Node);         
            
            #if (Node.Type in Event_Vwords_tags_set) or (Node.Type in State_Vwords_tags_set):
            #    Temp_parser.append(Node);
            #else:
            #    Temp_parser = [];
            #    self.CAG_Graph.append(Node);
            #index+=1;
            #for Node in self.CAG_Graph:
            #     if Node.Type in RB_Vwords_tags_set:
            #...

    def fitEvent(self,Temp_parser):
        for iterator in Temp_parser[1:-1]:
            if iterator.Type not in Event_Vwords_tags_set:
               return False;
        return True;       

    def fitState(self,Temp_parser):
        for iterator in Temp_parser[1:-1]:
            if iterator.Type not in State_Vwords_tags_set:
               return False;
        return True;              

    def plot_graph(self):
        if len(self.CAG_tokens)==0:
           return;
        graph = '['+self.CAG_tokens[0][0]+','+self.CAG_tokens[0][1]+']';   
        for index in range(len(self.CAG_tokens[0:-1])):
           graph+= Line_Dict[self.CAG_tokens[index][1]+'_'+self.CAG_tokens[index+1][1]] + '['+self.CAG_tokens[index+1][0]+','+self.CAG_tokens[index+1][1]+']';
        print graph   

                           

def TEST__construct_CAG():
    sentence = "we will implement deep learning algorithms with very simple codes";
    cag = CAG();
    cag.read_sentence(sentence);
    print cag.CAG_tokens;
    cag.plot_graph();
    #for soko in cag.CAG_Graph:
    #    print soko.text;



if __name__ == "__main__":
    TEST__construct_CAG();        


