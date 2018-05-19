#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import re
import csv
import sys
import nltk

class GraphNode(object):
    """Node in CAG"""
    type = "";
    text = "";
    Linked_Nodes = []; #其中的元素为turple:(Node类型,edge类型);
    #def __init__(self, arg):
    #    super(GraphNode, self).__init__();
    #    self.arg = arg;

    def __init__(self,type,text):
        if type == "Event":
            self.text = "Event";
            self.type = "Event";
            return 0;
        if type == "State":
            self.text = "State";
            self.type = "State";
            return 0;
        self.type = type;
        self.text = text;

    #def __init__(self,type,Event):
    #    if type == "Event":
    #        self.text = "Event";
    #        self.type = "Event";
    #    if type == "State":
    #        self.text = "State";
    #        self.type = "State";
            

    def link(self,another_node):
        Linked_Nodes.append((another_node,self.Edge_type(another_node)));    

    def Edge_type(self,another_node):
        return self.type + "__" + another_node.type;

Event_Vwords_tags_set = ['VBP','RB','VB','MD'];
State_Vwords_tags_set = ['RB','VBZ','MD'];
Union_Vwords_tags_set = [];
RB_Vwords_tags_set = [];

Con_tags_set = ['JJ','NN','NNS','NNP','DT','PRP','VBG'];
In_tags_set  = ['IN'];

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
        #self.link_all();     

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
            if token[1] in In_tags_set: #如果是副词
                if CAG_token[0]!="" and CAG_token[1]=="In": #承上：上一个词也是副词
                    if index<len(tokens)-1 and tokens[index+1][1] in In_tags_set:CAG_token[0] += " "+token[0];index +=1;continue; #启下：如果下一个也是副词
                    else:CAG_token[0] += " "+token[0];self.CAG_tokens.append(CAG_token);CAG_token = ["",""];index +=1;continue; #启下：如果下一个不是副词，此乃最后一个
                else:  #承上：上一个词不是副词
                    if index<len(tokens)-1 and tokens[index+1][1] in In_tags_set:CAG_token[0]=token[0];CAG_token[1]="In";index +=1;continue; #启下：如果下一个也是副词
                    else:CAG_token[0]=token[0];CAG_token[1]="In";self.CAG_tokens.append(CAG_token);CAG_token = ["",""];index +=1;continue; #启下：如果下一个也不是副词，此乃一个

            if token[1] in Con_tags_set: #如果是概念词
                if CAG_token[0]!="" and CAG_token[1]=="Con": #承上：上一个词也是概念词
                    if index<len(tokens)-1 and tokens[index+1][1] in Con_tags_set:CAG_token[0] += " "+token[0];index +=1;continue; #启下：如果下一个也是概念词
                    else:CAG_token[0] += " "+token[0];self.CAG_tokens.append(CAG_token);CAG_token = ["",""];index +=1;continue; #启下：如果下一个不是概念词，此乃最后一个
                else:  #承上：上一个词不是概念词
                    if index<len(tokens)-1 and tokens[index+1][1] in Con_tags_set:CAG_token[0]=token[0];CAG_token[1]="Con";index +=1;continue; #启下：如果下一个也是概念词
                    else:CAG_token[0]=token[0];CAG_token[1]="Con";self.CAG_tokens.append(CAG_token);CAG_token = ["",""];index +=1;continue; #启下：如果下一个也不是概念词，此乃一个
            if token[1] == 'RB': #'very simple code'
                if tokens[index+1][1] in Con_tags_set:CAG_token[0]=token[0];CAG_token[1]="Con";index +=1;continue; #启下：如果下一个是概念词       
                    
            self.CAG_tokens.append(token);
            index +=1;            
        
    def link_all(self):
        if self.sentence == "":
            return 0;
        for token in self.CAG_tokens:
            self.CAG_Nodes.append(GraphNode(token[1],token[0]));
        Temp_parser = []
        index       = 0
        for Node in reversed(self.CAG_Nodes): #逆序遍历才能解决"I think you should work harder!"
            if Node.type == "Con":
                if len(Temp_parser) > 1:
                    if self.fitEvent(Temp_parser):
                       Temp_parser.append(Node);
                       self.CAG_Graph.append(node("Event",Temp_parser)); #This Event linked nodes in Temp_parser of self.nodes?
                       Temp_parser = [];
                    if self.fitState(Temp_parser):
                       Temp_parser.append(Node);
                       self.CAG_Graph.append(node("State",Temp_parser)); #This Event linked nodes in Temp_parser of self.nodes?
                       Temp_parser = [];
                else:
                    Temp_parser.append(Node);       
            if (Node.type in Event_Vwords_tags_set) or (Node.type in State_Vwords_tags_set):
                Temp_parser.append(Node);
            else:
                Temp_parser = [];
                self.CAG_Graph.append(Node);
            index+=1;
            #for Node in self.CAG_Graph:
            #     if Node.type in RB_Vwords_tags_set:
            #...

    def fit(self,Temp_parser):
        pass;            
                           

def TEST__construct_CAG():
    sentence = "we will implement deep learning algorithms with very simple codes";
    cag = CAG();
    cag.read_sentence(sentence);
    print cag.CAG_tokens;
    #for soko in cag.CAG_tokens:
    #    print soko;


if __name__ == "__main__":
    TEST__construct_CAG();        


