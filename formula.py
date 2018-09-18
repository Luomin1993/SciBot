#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import *;
import numpy as np;
from Queue import Queue;

"""
np.random.randint(low=0, high=3);
"""

class Node(object):
    """Node in the Formula Graph"""
    def __init__(self, sym_expr):
        super(Node, self).__init__();
        self.sym_expr = sym_expr; # sympy instance;
        self.id  =  self.encode(self.sym_expr);
        self.sub_node_ids = [encode(sub_expr) for sub_expr in self.sym_expr.args];

    def encode(self,sym_expr):
        queue_exprs = Queue();
        queue_exprs.put(sym_expr);
        encode = [];
        while not queue_exprs.empty() :
            now_expr = queue_exprs.get();
            if len(now_expr.args)>0:
                for sub_expr in now_expr.args:
                    queue_exprs.put(sub_expr);
            encode.append(now_expr.__class__.__name__);
        return encode;

class Graph(object):
    """the Formula Graph"""
    def __init__(self, id ):
        super(Graph, self).__init__();
        self.id = id;
        self.Nodes = [];

    def make_edges(self):
        self.edges = [];
        for i in range(len(self.graph)):    
            for j in range(len(self.graph)):
                if graph[j].id in graph[i].sub_node_ids:
                    # which means an edge from node i to node j;
                    edges.append((i,j));
                    



#=============== make data =================
SYM_SET_VAR  = ['y','z','a','b','u'];
SYM_SET_FUNC = ['g','h','n','m','k', 'Env', 'Kar','Pt','Pm','Pr','Qam','Lamma','Y0'];
OPT_SET_ONE  = ['exp','sin','cos','exp','gamma'];
OPT_SET_TWO  = ['diff','integrate','','exp','gamma'];

def make_random_sym_var():
    x  = Symbol(SYM_SET_VAR[ np.random.randint(low=0,high=len(SYM_SET_VAR)) ]);
    return x;

def make_random_sym_func():
    x  = symbols(SYM_SET_FUNC[ np.random.randint(low=0,high=len(SYM_SET_FUNC)) ],cls=Function);
    return x;

def make_random_func(n,x):
    f = make_random_sym_func();
    f = f(x);
    for i in range(n):
        m = np.random.randint(low=1,high=10)
        if m%3==1: f1=make_random_sym_func();f += f1(x);
        if m%3==2: f1=make_random_sym_func();f *= f1(x);
        if m%3==0: f1=make_random_sym_func();f  = f1(f);
    return f;


def make_random_int(x):
    f  = make_random_func(np.random.randint(low=1,high=3),x);
    return integrate(f,x);

def make_random_diff(x):
    f  = make_random_func(np.random.randint(low=1,high=3),x);
    return diff(f,x);

def make_random_poly(x):
    m  = np.random.randint(low=1,high=5);
    expr = (np.random.random()-0.5)*2000;
    for i in range(m):
        if np.random.randint(low=1,high=6)%2:expr += (np.random.random()-0.5)*2000* x**(np.random.randint(low=1,high=4));
        else:expr *= (np.random.random()-0.5)*2000* x**(np.random.randint(low=1,high=4));
    return expr;

def make_random_eq(n):
    lhs = make_random_int(make_random_sym_var());
    rhs = make_random_func(np.random.randint(low=1,high=3),make_random_sym_var());
    for i in range(n):
        m = np.random.randint(low=1,high=10)
        if m%3==1: f1=make_random_sym_func();f2=make_random_sym_func();lhs += f1(make_random_sym_var());rhs += f1(make_random_sym_var());
        if m%3==2: f1=make_random_sym_func();f2=make_random_sym_func();lhs *= f1(make_random_sym_var());rhs *= f1(make_random_sym_var());
        if m%3==0: f1=make_random_sym_func();f2=make_random_sym_func();lhs  = f1(lhs);rhs  = f1(lhs);
    return Eq(lhs,rhs);

def make_random_diff_eq():
    f = Function('f');
    x = Symbol('x');
    forward_0 = make_random_sym_var()*make_random_sym_func()(make_random_sym_var());
    forward_1 = make_random_sym_var()*make_random_sym_func()(make_random_sym_var());
    forward_2 = make_random_sym_var()*make_random_sym_func()(make_random_sym_var());
    lhs = forward_2*f(x).diff(x, x) + forward_1*f(x).diff(x) + forward_0*f(x);
    rhs = make_random_sym_var()**np.random.randint(low=0,high=3)*make_random_sym_func()(x);
    diffeq = Eq(lhs,rhs);
    #return dsolve(diffeq,f(x));
    return diffeq,dsolve(diffeq,f(x));

def make_to_file():
    f = open('data.fm','w');
    for i in range(50):
        print float(i)/50;
        f.write( '------------------\n');
        diffeq,solveeq=make_random_diff_eq();
        f.write(srepr(diffeq) +'\n');
        f.write(srepr(solveeq) +'\n');
    f.close();

def F2G(F_s):
    queue_exprs = Queue();
    F_s=F_s.replace('\'','"');
    exec 'F ='+F_s;
    queue_exprs.put(F);
    #self.__class__.__name__;self.name;
    #print make_random_sym_func().__name__;
    graph = [];
    while not queue_exprs.empty() :
        now_expr = queue_exprs.get();
        if len(now_expr.args)>0:
            for sub_expr in now_expr.args:
                queue_exprs.put(sub_expr);
        #print now_expr.__class__.__name__;
        new_node = Node(now_expr);
        if new_node.id not in graph: graph.append(new_node.id);
    print len(graph);

if __name__ == '__main__':
    #print make_random_poly(make_random_sym_var());
    #print make_random_sym_var().__class__.__name__;
    #print make_random_sym_var().name;
    #print make_random_sym_func().__name__;
    #print make_random_eq(3);
    #for i in range(5):print make_random_diff_eq();
    #make_to_file();
    #print F2G(srepr(make_random_diff_eq()[0]));
    F2G("Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Rational(1, 2),sin(Mul(Symbol('x'), Symbol('y')))), Pow(Symbol('y'), Integer(-1)))");
