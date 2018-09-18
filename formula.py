#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import *;
import numpy as np;

"""
np.random.randint(low=0, high=3);
"""

class Node(object):
    """Node in the Formula Graph"""
    def __init__(self, id, sym):
        super(Node, self).__init__();
        self.id  =  id;
        self.sym = sym; # sympy instance;
        self.sub_Nodes = [];



class Graph(object):
    """the Formula Graph"""
    def __init__(self, id ):
        super(Graph, self).__init__();
        self.id = id;
        self.Nodes = [];


#=============== make data =================
SYM_SET_VAR  = ['x','y','z','a','b','u'];
SYM_SET_FUNC = ['f','g','h','n','m','k', 'Env', 'Kar','Pt','Pm','Pr','Qam','Lamma','Y0'];
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


if __name__ == '__main__':
    #print make_random_poly(make_random_sym_var());
    #print make_random_func(3);
    print make_random_eq(3);
