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
            #print(len(level_nodes));
            for node in level_nodes:
                print(node.string+' ',end=' ');
            print('\n');
            for node in level_nodes:
                print(' '+'|',end=' ');    
            print('\n');

    def print_as_array(self):
        arr = [];
        for level_nodes in self.Graph:
            arr.append([]);
            for node in level_nodes:
                arr[-1].append(node.string);
        print(arr);        

    def construct_graph(self):
        pass;

    def link_symbol(self):
        pass;                

    def is_full(self):
        turple_num = 0;
        pow_num    = 0;
        for i in range(len(self.Graph)):
            for j in self.Graph[i]:
                turple_num +=1;                
            #pow_num += 2**i;    
        for i in range(self.deepth):
            pow_num += 2**i;    
        return turple_num == pow_num;     

    def random_construct_graph(self):
        num_opt = np.random.randint(5)+3;
        num_sym = np.random.randint(5)+3;
        this_level = 0;
        secure_infine_circle = 222;
        while not(self.is_full()):
        	# if it's the root;
            if len(self.Graph) == 0:
                self.Graph.append( [Node(attr='root', string=OPT[np.random.randint(len(OPT))], code=0, level=0,opt_num=np.random.randint(2)+1,ID=(0,0)) ] );
                num_opt -=1;
                this_level += 1;
                self.Graph.append([]);
                continue;
            # judge if the level needs change;
            if len(self.Graph[-1])>0 and len(self.Graph[-1]) == 2**(len(self.Graph)-1):
                # print(str(len(self.Graph[-1])) + ' : ' + str(2**(len(self.Graph))))
                this_level += 1;
                if this_level>self.deepth:break;
                self.Graph.append([]);
                continue;
            # decide this node is sym/opt/...
            if num_opt>0 or num_sym>0:
                this_node = Node(attr=ATTR[np.random.randint(2)]);
                if this_node.attr=='sym' and num_sym>0:
                    this_node.string  = SYM[np.random.randint(len(SYM))];
                    this_node.level   = this_level;
                    this_node.opt_num = 0;
                    this_node.ID = (this_level,len(self.Graph[-1]));
                    num_sym -=1;
                if this_node.attr=='opt' and num_opt>0:
                    this_node.string  = OPT[np.random.randint(len(OPT))];
                    this_node.level   = this_level;
                    this_node.opt_num = np.random.randint(2)+1;
                    this_node.ID = (this_level,len(self.Graph[-1]));
                    num_opt -=1;    
                # preventing the last layer is opt;
                if this_level==self.deepth and this_node.attr=='opt':
                    continue;
                # get the choice but no more num...
                if (this_node.attr=='sym' and num_sym==0 and num_opt>0) or (this_node.attr=='opt' and num_opt==0 and num_sym>0):
                    continue;

            # link this node to the right prev node:
            for i in range( len(self.Graph[-2]) ):
                # Link/Add the constructed node into Graph:
                if self.Graph[-2][i].opt_num>0 and self.Graph[-2][i].opt_num>len(self.Graph[-2][i].next):
                    self.Graph[-2][i].next.append(this_node.ID);
                    self.Graph[-1].append(this_node);
                    break;
                # Link/Add the dummy node into Graph:
                while 2 > len(self.Graph[-2][i].next) and self.Graph[-2][i].opt_num <= len(self.Graph[-2][i].next):
                    dummy_node = Node(attr='dummy',opt_num=0,ID = (this_level,len(self.Graph[-1])) );
                    self.Graph[-2][i].next.append(dummy_node.ID);
                    self.Graph[-1].append(dummy_node);
            """

            # link this node to the right prev node:
            if len(self.Graph[-1]) < 2**(this_level-1):
                # find which node's next_arr is not full:
                find_one = 0;
                for i in range( len(self.Graph[-2]) ):
                	# Link/Add the constructed node into Graph:
                    if self.Graph[-2][i].opt_num>0 and self.Graph[-2][i].opt_num>len(self.Graph[-2][i].next):
                        self.Graph[-2][i].next.append(this_node.ID);
                        self.Graph[-1].append(this_node);
                        find_one =1;
                    # Link/Add the dummy node into Graph:
                    if 2 > len(self.Graph[-2][i].next) and self.Graph[-2][i].opt_num==len(self.Graph[-2][i].next):
                        dummy_node = Node(attr='dummy',opt_num=0,ID = (this_level,len(self.Graph[-1])) );
                        self.Graph[-2][i].next.append(dummy_node.ID);
                        self.Graph[-1].append(dummy_node);
                        find_one =1;
                    if find_one:break;    
            """        
            # Prevent falling into an infinite cycle;
            secure_infine_circle -= 1;
            if secure_infine_circle==0:break;

    def change_by_code(self,opt_code):
        pass;



# -------------- T E S T -----------------
if __name__ == '__main__':
    for i in range(200):
        gg = FormulaGraph(4);
        gg.random_construct_graph();
        #gg.draw();
        gg.print_as_array();


# -------------- P R O B L E M ----------
"""
[['-'], ['∧', '∧'], ['√', '√', '0', 'ε'], ['β', '0', '0', '0', '0', '0']]
[['∨'], ['∧', '√'], ['∧', '∧', 'α', 'α'], ['λ', '0', '0', '0']]
[['∕'], ['∕', '∧'], ['ι', 'ι', '0', 'λ'], ['0', '0', '0', '0', '0', '0']]
[['∨'], ['-', '∇'], ['∨', '∨', '0', '0'], ['κ', '0', '0', '0', '0', '0']]
[['∇'], ['∕', '∧'], ['∨', '∨', '0', 'ι'], ['κ', '0', '0', '0', '0', '0']]
[['∧'], ['∨', '∇'], ['ν', 'ν', 'κ', '0'], ['0', '0', '0', '0', '0', '0']]
[['∧'], ['-', '×'], ['ε', 'ε', '0', 'ν'], ['0', '0', '0', '0', '0', '0']]
[['×'], ['γ', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]
[['∇'], ['+', '∇'], ['∨', '∨', 'θ', '0'], ['η', 'η', '0', '0', '0', '0']]
[['∕'], ['∨', '∇'], ['ι', 'ι', 'ι', '0'], ['0', '0', '0', '0', '0', '0']]
[['√'], ['∇', '√'], ['∧', '∧', 'ε', '0'], ['×', '0', '0', '0', '0', '0']]
[['∨'], ['+', '+'], ['δ', 'δ', '0', 'ν'], ['0', '0', '0', '0', '0', '0']]
[['√'], ['-', '∨'], ['γ', 'γ', '0', 'κ'], ['0', '0', '0', '0', '0', '0']]
[['×'], ['∕', '√'], ['∧', '∧', '0', '0'], ['δ', '0', '0', '0', '0', '0']]
[['-'], ['+', '∇'], ['α', 'α', '0', '0'], ['0', '0', '0', '0', '0', '0']]
[['×'], ['+', '∨'], ['η', 'η', '0', 'ζ'], ['0', '0', '0', '0', '0', '0']]
[['∕'], ['+', '∧'], ['∧', '∧', '∨', '∨'], ['∨', '∨', '∨', '0']]
[['∨'], ['∨', '∧'], ['β', 'β', '×', '×'], ['0', '0', 'β', '0']]
[['√'], ['-', '√'], ['β', 'β', '√', '√'], ['0', '0', 'η', '0']]
[['×'], ['∧', '∇'], ['ζ', 'ζ', '0', '0'], ['0', '0', '0', '0', '0', '0']]
[['√'], ['+', '∨'], ['×', '×', 'κ', 'κ'], ['θ', 'θ', '0', '0']]
[['∇'], ['√', '∕'], ['+', '+', 'ε', '0'], ['ε', '0', '0', '0', '0', '0']]
[['-'], ['√', '×'], ['∨', '∨', '0', '0'], ['∇', '∇', '0', '0', '0', '0']]
[['∧'], ['+', '∨'], ['λ', 'λ', '0', 'β'], ['0', '0', '0', '0', '0', '0']]

"""        