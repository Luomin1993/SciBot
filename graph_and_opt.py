#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np;

"""
∇ ∈ ∝ ∧ ∨ ～ ∫ ≠ ≤ ≥ ≈ ∞ π
α β γ δ ε ζ η θ ι κ λ μ ν 
∈ ∏ ∑ ∕ √ ∝ ∞ ∟ ∠ ∣ ∥ ∧ ∨ ∩ ∪ ∫ ∮ ÷ × ± 
"""

OPT = ['+','-','×','∕','√','∧','∨','∇'];

JUD = ['≠','≤','≥','∕','√','∈'];

SYM = ['α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν'];

ATTR = ['sym','opt'];

class Node(object):
    """docstring for Node"""
    def __init__(self, attr='sym', string='0', code=-1, level=-1,opt_num=-1,ID=-1):
        super(Node, self).__init__()
        self.attr    =    attr;
        self.string  =  string;
        self.code    =    code;
        self.level   =   level;
        self.opt_num = opt_num;
        self.next    =      [];
        self.prev    =      -1;
        self.ID      =      ID; # (level,No.)

    def get_next_num(self):
        return len(self.next);

    def set_as_next(self,next_node):
        self.next.append(next_node);

    def set_as_prev(self,prev_node):
        self.prev = prev_node;

    def dis_link(self,linked_node):
        for node in self.next:
            if self.same_as(node):
               del self.next[ self.next.index(node.ID) ];

    def same_as(self,another_node):
        if (self.attr == another_node.attr) and (self.string == another_node.string) and (self.attr == 'sym'):
            return True;

        if (self.ID == another_node.ID):
            return True;
        return False;

class FormulaGraph(object):
    """docstring for FormulaGraph"""
    def __init__(self, deepth):
        super(FormulaGraph, self).__init__()
        self.deepth  = deepth;
        self.set_opt = [];
        self.set_jud = [];
        self.set_sym = [];
        self.Graph   = [];
    
    def draw(self):
        for level_nodes in self.Graph:
            for node in level_nodes:
                print(node.string+' ');
            for node in level_nodes:
                print(' '+'|');    

    def construct_graph(self):
        pass;

    def link_symbol(self):
        pass;                

    def random_construct_graph(self):
        num_opt = np.random.randint(3)+3;
        num_sym = np.random.randint(3)+3;
        this_level = 0;
        while num_opt!=0 and num_sym != 0:
            if len(self.Graph) == 0:
                self.Graph.append( [Node(attr='root', string=OPT[np.random.randint(len(OPT))], code=0, level=0,opt_num=np.random.randint(1)+1,ID=(0,0)) ] );
                num_opt -=1;
                this_level += 1;
                self.Graph.append([]);
                continue;
            # judge if the level needs change;
            if len(self.Graph[-1]) == 2**len(self.Graph):
                this_level += 1;
                if this_level>self.deepth:break;
                self.Graph.append([]);
                continue;
            # decide this node is sym/opt/...
            if num_opt>0 and num_sym>0:
                this_node = Node(attr=ATTR[np.random.randint(1)]);
                if this_node.attr=='sym':
                    this_node.string  = SYM[np.random.randint(len(SYM))];
                    this_node.level   = this_level;
                    this_node.opt_num = 0;
                    this_node.ID = (this_level,len(self.Graph[-1]));
                    num_sym -=1;
                if this_node.attr=='opt':
                    this_node.string  = OPT[np.random.randint(len(OPT))];
                    this_node.level   = this_level;
                    this_node.opt_num = np.random.randint(1)+1;
                    this_node.ID = (this_level,len(self.Graph[-1]));
                    num_opt -=1;    
            # link this node to the right prev node:
            for i in range( len(self.Graph[-2]) ):
                # Link/Add the constructed node into Graph:
                if self.Graph[-2][i].opt_num>0 and self.Graph[-2][i].opt_num>len(self.Graph[-2][i].next):
                    self.Graph[-2][i].next.append(this_node.ID);
                    self.Graph[-1].append(this_node);
                # Link/Add the dummy node into Graph:
                if self.Graph[-2][i].opt_num>0 and self.Graph[-2][i].opt_num>len(self.Graph[-2][i].next):
                    dummy_node = Node(attr='dummy',ID = (this_level,len(self.Graph[-1])) );
                    self.Graph[-2][i].next.append(dummy_node.ID);
                    self.Graph[-1].append(dummy_node);

# -------------- T E S T -----------------
if __name__ == '__main__':
    gg = FormulaGraph(3);
    gg.random_construct_graph();
    gg.draw();