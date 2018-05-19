/*
Created on Wed Apr 04 22:02:19 2018

@author: Hanss401

*/


#include <iostream>
#include <vector>
#include <map>
//#include "tree.hpp"

#define MAX_USE_SYM 100

using namespace std;

//--------------------------  Using Struct ---------------------------------
/*class AAA
{
public:	
	//std::vector<Node*> SubNodes;
	string sym;
	virtual string show(){return sym;}
};

class Node //:public AAA
{
public:	
	std::vector<Node*> SubNodes;
	string expression;
public:
	Node(string symbol){expression = symbol;}
	virtual string show(){return expression;}
};

class Sym:public Node
{
public:
	string expression;
public:	
    Sym(string symbol):Node("string symbol"){expression = symbol;}
    string show() override{return expression;}	
};

class Add:public Node
{
public:
	string expression;
public:
	std::vector<Node*> SubNodes;
	Add(Node s1,Node s2):Node("string symbol"){SubNodes.push_back(&s1);SubNodes.push_back(&s2);expression = "("+SubNodes[0]->expression+" + "+SubNodes[1]->expression+")";}
	string show() override{return "("+SubNodes[0]->show()+" + "+SubNodes[1]->show()+")";}
};


*/
//--------------------------------------------------------------------------------------------
//------------------------------                             ---------------------------------
//------------------------------  Using functions to realize ---------------------------------
//------------------------------                             ---------------------------------
//--------------------------------------------------------------------------------------------
struct Node
{
	string type;
	string symbol;
	string expression;
	vector<Node*> SubNodes;
	int subNodeNum;
	//Node(string exp){expression = exp;}
	/*Node(string typ,string sym,string exp,int subnn)
	{
		type       =    typ;
		expression =    exp;
		sym        = symbol;
		subNodeNum =  subnn;
	}*/
};

/*struct Node Sym;
Sym.type = "Sym";

struct Node Add;
Add.symbol = "+";
Add.type   = "compute";
*/



Node* sym(string exp)
{
	//static Node* sym = new Node;
	static std::vector<Node*> sym_statck;
	sym_statck.push_back(new Node);
	/*if (sym->expression!="")
	{
		cout<<"WTF"<<endl;
	}*/
	if (sym_statck.size()<MAX_USE_SYM)
	{
		int last = sym_statck.size()-1;
		sym_statck[last]->expression = exp;
		sym_statck[last]->type       = "Sym";
		return sym_statck[last];
	}
	return NULL;
	//sym->expression = exp;
}

Node* num(string exp)
{
	//static Node* num = new Node;
	static std::vector<Node*> num_statck;
	num_statck.push_back(new Node);
	/*if (num->expression!="")
	{
		cout<<"WTF"<<endl;
	}*/
	if (num_statck.size()<MAX_USE_SYM)
	{
		int last = num_statck.size()-1;
		num_statck[last]->expression = exp;
		num_statck[last]->type       = "Num";
		return num_statck[last];
	}
	return NULL;
	//num->expression = exp;
}

Node* add(Node* s1,Node* s2)
{
	static std::vector<Node*> add_stack;
	add_stack.push_back(new Node);
	if (add_stack.size()<MAX_USE_SYM)
	{
		int last = add_stack.size()-1;
		add_stack[last]->SubNodes.push_back(s1);
		add_stack[last]->SubNodes.push_back(s2);
		add_stack[last]->symbol     = "+";
		add_stack[last]->subNodeNum = add_stack[last]->SubNodes.size();
		add_stack[last]->expression = "("+s1->expression+"+"+s2->expression+")";
		return add_stack[last];
	}
	return NULL;

	/*static Node add;
	add.SubNodes.push_back(s1);
	add.SubNodes.push_back(s2);
	add.expression = "("+s1->expression+"+"+s2->expression+")";
	return &add;*/
}


Node* times(Node* s1,Node* s2)
{
	static std::vector<Node*> times_stack;
	times_stack.push_back(new Node);
	if (times_stack.size()<MAX_USE_SYM)
	{
		int last = times_stack.size()-1;
		times_stack[last]->SubNodes.push_back(s1);
		times_stack[last]->SubNodes.push_back(s2);
		times_stack[last]->expression = "("+s1->expression+"×"+s2->expression+")";
		return times_stack[last];
	}
	return NULL;
}

Node* equal(Node* s1,Node* s2)
{
	static std::vector<Node*> equal_stack;
	equal_stack.push_back(new Node);
	if (equal_stack.size()<MAX_USE_SYM)
	{
		int last = equal_stack.size()-1;
		equal_stack[last]->SubNodes.push_back(s1);
		equal_stack[last]->SubNodes.push_back(s2);
		equal_stack[last]->expression = s1->expression+" = "+s2->expression;
		return equal_stack[last];
	}
	return NULL;
}




//---------- Example of Pm Equation --------
Node* derivation(Node* s1,Node* s2)
{
	static std::vector<Node*> derivation_stack;
	derivation_stack.push_back(new Node);
	if (derivation_stack.size()<MAX_USE_SYM)
	{
		int last = derivation_stack.size()-1;
		derivation_stack[last]->SubNodes.push_back(s1);
		derivation_stack[last]->SubNodes.push_back(s2);
		derivation_stack[last]->expression = "∂"+s1->expression+"/∂"+s2->expression;
		return derivation_stack[last];
	}
	return NULL;
}



Node* sum(Node* s1)
{
	static std::vector<Node*> sum_stack;
	sum_stack.push_back(new Node);
	if (sum_stack.size()<MAX_USE_SYM)
	{
		int last = sum_stack.size()-1;
		sum_stack[last]->SubNodes.push_back(s1);
		//sum_stack[last]->SubNodes.push_back(s2);
		sum_stack[last]->expression = "∑"+s1->expression;
		return sum_stack[last];
	}
	return NULL;
}


Node* integral(Node* s1,Node* s2)
{
	static std::vector<Node*> integral_stack;
	integral_stack.push_back(new Node);
	if (integral_stack.size()<MAX_USE_SYM)
	{
		int last = integral_stack.size()-1;
		integral_stack[last]->SubNodes.push_back(s1);
		integral_stack[last]->SubNodes.push_back(s2);
		integral_stack[last]->expression = "∫"+s1->expression+"d"+s2->expression;
		return integral_stack[last];
	}
	return NULL;
}



Node* ln(Node* s1)
{
	static std::vector<Node*> ln_stack;
	ln_stack.push_back(new Node);
	if (ln_stack.size()<MAX_USE_SYM)
	{
		int last = ln_stack.size()-1;
		ln_stack[last]->SubNodes.push_back(s1);
		//ln_stack[last]->SubNodes.push_back(s2);
		ln_stack[last]->expression = "ln("+s1->expression+")";
		return ln_stack[last];
	}
	return NULL;
}


Node* exp(Node* s1)
{
	static std::vector<Node*> exp_stack;
	exp_stack.push_back(new Node);
	if (exp_stack.size()<MAX_USE_SYM)
	{
		int last = exp_stack.size()-1;
		exp_stack[last]->SubNodes.push_back(s1);
		//exp_stack[last]->SubNodes.push_back(s2);
		exp_stack[last]->expression = "exp("+s1->expression+")";
		return exp_stack[last];
	}
	return NULL;
}

Node* der(Node* s1)
{
	static std::vector<Node*> der_stack;
	der_stack.push_back(new Node);
	if (der_stack.size()<MAX_USE_SYM)
	{
		int last = der_stack.size()-1;
		der_stack[last]->SubNodes.push_back(s1);
		//der_stack[last]->SubNodes.push_back(s2);
		der_stack[last]->expression = "d"+s1->expression;
		return der_stack[last];
	}
	return NULL;
}

Node* sub(Node* s1,Node* s2)
{
	static std::vector<Node*> sub_stack;
	sub_stack.push_back(new Node);
	if (sub_stack.size()<MAX_USE_SYM)
	{
		int last = sub_stack.size()-1;
		sub_stack[last]->SubNodes.push_back(s1);
		sub_stack[last]->SubNodes.push_back(s2);
		sub_stack[last]->expression = s1->expression+"-"+s2->expression;
		return sub_stack[last];
	}
	return NULL;
}

Node* devide(Node* s1,Node* s2)
{
	static std::vector<Node*> devide_stack;
	devide_stack.push_back(new Node);
	if (devide_stack.size()<MAX_USE_SYM)
	{
		int last = devide_stack.size()-1;
		devide_stack[last]->SubNodes.push_back(s1);
		devide_stack[last]->SubNodes.push_back(s2);
		devide_stack[last]->expression = s1->expression+"/"+s2->expression;
		return devide_stack[last];
	}
	return NULL;
}


//mapStudent.insert(map<int, string>::value_type (1, "student_one"));
//namespace method
static std::map<Node*,Node*> Methods;







//-------------------------------------
//
//the formula generator function;
//
//-------------------------------------
//
//map_turples(Node* real_tree,Node* template_tree,map<Node*,Node*>& turpleMap):  
//   find the one-one turple in the real tree and the template tree; 
//
//replace(Node* real_tree,Node* template_tree,const map<Node*,Node*> turpleMap):
//   do replace one-one turple on the second tree;   
//
//compare(Node* real_tree,Node* template_tree):
//   find if the template_tree is the sub-tree of the real_tree,and from where(Start) they are the same;
//
//


//deduce process: let state_1 do action like : template_state_1 ----> template_state_2;
//
Node* do_deduce(Node* state_1,const Node* template_state_1,const Node* template_state_2)
{}


typedef std::vector<Node*> deduce_chain;

void make_deduce_chain(deduce_chain& Chain_to_make,const deduce_chain Chain_template)
{}







void signin(std::map<Node*,Node*>& Methods)
{
	//std::map<Node*,Node*> Methods;

	// move item
	static Node* move_item_key   = equal(sym("a") , sub(sym("b"),sym("c")));
	static Node* move_item_value = equal(add(sym("a"),sym("c")) , sym("b"));
	//Methods.insert(map<Node*,Node*>::value_type (move_item_key,move_item_value));
	Methods[move_item_key]       = move_item_value;
	Methods[move_item_value]     = move_item_key;

	// times devide
	static Node* times_devide_key   = equal(sym("a") , devide(sym("b"),sym("c")));
	static Node* times_devide_value = equal(times(sym("a"),sym("c"))  ,sym("b"));
	Methods[times_devide_key]       = times_devide_value;
	Methods[times_devide_value]     = times_devide_key;

	// int de
	static Node* int_de_key   = integral(sym("f")  ,sym("x"));
	static Node* int_de_value = derivation(sym("f"),sym("x"));
	Methods[int_de_key]       = int_de_value;
	Methods[int_de_value]     = int_de_key;

	// int
	static Node* int_by_sides_A_key   = equal(times(sym("f"),der(sym("x"))), der(sym("t")));
	static Node* int_by_sides_A_value = equal(integral(sym("f"),der(sym("x"))), sym("t"));
	Methods[int_by_sides_A_key]       = int_by_sides_A_value;

	static Node* special_int_key      = equal(integral(devide(num("1"),sub(sym("S"),times(sym("a"),sym("N")))),sym("N")) ,
		                                                                                     integral(num("1"),sym("t")) );
	static Node* special_int_value    = equal(add(times(devide(num("-1"),sym("a")),ln(sub(sym("S"),times(sym("a"),sym("N"))))),sym("C")), sym("t"));
	Methods[special_int_key]          = special_int_value;


	// 

}


void TEST_expression_int()
{
	signin(Methods);
	cout<<(--Methods.end())->first->expression<<endl;
	cout<<(--Methods.end())->second->expression<<endl;
	//cout<<special_int_value->expression<<endl;
}

//static Node* expression_test = equal(derivation(sym("N"),sym("t")) , sym("N\'") );

void TEST_expression()
{
	static Node* expression_test = equal(derivation(sym("N"),sym("t")) , sym("N\'") );
	cout<<expression_test->expression<<endl;
}




/*int main(int argc, char const *argv[])
{
	//cout<<Add(Sym("A"),Sym("B")).SubNodes[]<<endl;
	//cout<<Add(Sym("A"),Sym("B")).expression<<endl;
	//Node a = Sym("A");Node b = Sym("B");
	//cout<<Add(a,b).show()<<endl;
	//cout<<Sym("B").show()<<endl;
	
	//cout<<add(sym("a"),add(sym("b"),sym("c")) )->expression<<endl;
	//cout<<expression_test->expression<<endl;
	TEST_expression_int();
	return 0;
}*/