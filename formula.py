# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 19:08:19 2017

@author: Hanss401
"""
#/usr/local/lib/python2.7/dist-packages/sympy
#np.random.randint(low=0, high=3)


from __future__ import division;
from sympy import *;
import numpy as np;
init_printing(use_unicode=True)

'''
def Sym(x):
    return Node( Symbol(x) );

def Add(x1,x2):
    return Node( x1+x2 );

def Sub(x1,x2):
    return Node( x1-x2);

def Times(x1,x2):
    return Node( x1*x2 );

def Div(x1,x2):
    return Node( x1/x2 );

def Pow(x1,x2):
    return Node( x1**x2);

def Exp():    
'''

#=========== SET ================
#OPT_SET_TWO     = ['Add','Mul','Pow']#,'Integral','Derivative'];
#OPT_SET_ONE     = ['sin','cos','tan','exp'];
OPT_SET_ONE     = [sin,cos,tan,exp];
SYMBOL_VAR_SET  = ['x','y','z','k'];
SYMBOL_FUNC_SET = ['f','g','m','n'];

# #======= make dataset OLD===========

# def make_random_int():
#     x   = Symbol(SYMBOL_VAR_SET[ np.random.randint(low=1, high=len(SYMBOL_VAR_SET)) ]);
#     f   = OPT_SET_ONE[ np.random.randint(low=1, high=len(OPT_SET_ONE)) ](x);
#     return Integral(f,x);

# def make_random_diff():
#     x   = Symbol(SYMBOL_VAR_SET[ np.random.randint(low=1, high=len(SYMBOL_VAR_SET)) ]);
#     f   = OPT_SET_ONE[ np.random.randint(low=1, high=len(OPT_SET_ONE)) ](x);
#     return Derivative(f,x);

# def make_random_poly():
#     x   = Symbol(SYMBOL_VAR_SET[ np.random.randint(low=1, high=len(SYMBOL_VAR_SET)) ]);
#     n   = np.random.randint(low=1, high=4);
#     f   = (np.random.random()-0.5)*2000;
#     for i in range(n):
#         f += (np.random.random()-0.5)*200*Pow(x,np.random.randint(low=1, high=4));
#     return f;    

# def make_random_func():
#     x = make_random_poly();
#     f = OPT_SET_ONE[ np.random.randint(low=1, high=len(OPT_SET_ONE)) ](x);
#     return f;    

# def make_random_cat(x1,x2):
#     n  = np.random.randint(low=1, high=4);
#     if n==1:return x1+x2;
#     if n==2:return x1-x2;
#     if n==3:return x1*x2;
#     if n==4:return -x1*x2;


# class Sample_Der_Process(object):
#     """A Sample_Der_Process"""
#     def __init__(self):
#         super(Sample_Der_Process, self).__init__()
#         self.F_t = None;
#         self.Processes = [];        

# def make_a_sample():
#     exec 'expr_r = '+OPT_SET_TWO[np.random.randint(low=1, high=len(OPT_SET_TWO))]+'(Symbol("'+ SYMBOL_VAR_SET[np.random.randint(low=1, high=len(SYMBOL_VAR_SET))] +'"),Symbol("'+ SYMBOL_VAR_SET[np.random.randint(low=1, high=len(SYMBOL_VAR_SET))] +'"))';
#     # print expr_r;
#     exec 'expr_l = '+OPT_SET_TWO[np.random.randint(low=1, high=len(OPT_SET_TWO))]+'(Symbol("'+ SYMBOL_VAR_SET[np.random.randint(low=1, high=len(SYMBOL_VAR_SET))] +'"),Symbol("'+ SYMBOL_VAR_SET[np.random.randint(low=1, high=len(SYMBOL_VAR_SET))] +'"))';
#     # print expr_l;
#     for i in range(5):
#         exec 'expr_l = '+OPT_SET_TWO[np.random.randint(low=1, high=len(OPT_SET_TWO))]+'( '+OPT_SET_ONE[np.random.randint(low=1, high=len(OPT_SET_ONE))]+'(expr_l),Symbol("'+ SYMBOL_VAR_SET[np.random.randint(low=1, high=len(SYMBOL_VAR_SET))] +'"))';
#         exec 'expr_r = '+OPT_SET_TWO[np.random.randint(low=1, high=len(OPT_SET_TWO))]+'( '+OPT_SET_ONE[np.random.randint(low=1, high=len(OPT_SET_ONE))]+'(expr_r),Symbol("'+ SYMBOL_VAR_SET[np.random.randint(low=1, high=len(SYMBOL_VAR_SET))] +'"))';
#     #print srepr(Eq(expr_l,expr_r));    
#     steps = [];
#     while 1:
#         steps.append(   Eq(expr_l,expr_r)  );
#         res = next_step(expr_l,expr_r);
#         if res==0:break;
#         print str(res[0])+' = '+str(res[1]);
#         (expr_l,expr_r) = res;
#     for step in steps:print step;    

#===== make dataset ===========
SYM_SET_VAR  = ['x','y','z','a','b','u'];
SYM_SET_FUNC = ['f','g','Ho','Nt','Ms','KL', 'Env', 'Kar','Pt','Pm','Pr','Qam','Lamma','Y0'];
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



#===== data structure ==================

class Node(object):
    """Node in the Graph"""
    def __init__(self, sym):
        super(Node, self).__init__()
        self.id       = 0;
        self.sym      = sym;    
        self.subNodes = [];
        #self.func     = Sym;


class Graph(object):
    """the Formula Graph"""
    def __init__(self, id):
        super(Graph, self).__init__()
        self.id    = id;
        self.Nodes = [];
        self.exp   = [];

#======== helper functions ==========
def next_step(expr_l,expr_r):
    while len(expr_r.args)>=2:
        if len(expr_r.args[1].args)>len(expr_r.args[0].args) : 
            expr_l = solveset(Eq(expr_l, expr_r), expr_r.args[1]).args[0];
            return (expr_l,expr_r.args[1]);
        else : 
            expr_l = solveset(Eq(expr_l, expr_r), expr_r.args[0]).args[0];
            return (expr_l,expr_r.args[0]);
    return 0;

    

#======= TEST ============
def test_next_step(Fe):
    expr_l = Fe.args[0];
    expr_r = Fe.args[1];
    i=10;
    while i>0:
        print Fe;
        Fe = next_step(expr_l,expr_r);
        if Fe==0:break;
        print str(Fe[0])+' = '+str(Fe[1]);
        (expr_l,expr_r) = Fe;
        i-=1;


def test_solve_one():
	#ConditionSet(b, Eq(Pm(b) - Y0(Pr(a)), 0), Reals)
    a,b      = symbols('a b',real=True);
    Pm,Y0,Pr = symbols('Pm Y0 Pr',cls=Function);
    lhs = Pm(b);
    rhs = Y0(Pr(a));
    Fe = Eq(lhs,rhs);
    #print lhs.args;
    return solveset(Fe,b,domain=S.Reals);



if __name__ == '__main__':
    #exec 'print Mul(Symbol(\'a\'), Symbol(\'y\'))';
    #exec 'print Mul(Symbol("a"), Symbol("y"))';        
    #test_next_step();
    #make_a_sample();
    #print make_random_int();
    #print make_random_func();
    #print make_random_diff();
    #print make_random_cat(make_random_func(),make_random_func());
    #print make_random_eq(3);
    #test_next_step(make_random_eq(3));
    print test_solve_one().args[0];