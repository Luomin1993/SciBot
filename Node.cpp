#include <iostream>
#include <vector>
#include <map>

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

//------------------------------  Using functions to realize ---------------------------------
struct Node
{
	string type;
	string symbol;
	string expression;
	vector<Node*> SubNodes;
	//Node(string exp){expression = exp;}
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

Node* add(Node* s1,Node* s2)
{
	static std::vector<Node*> add_stack;
	add_stack.push_back(new Node);
	if (add_stack.size()<MAX_USE_SYM)
	{
		int last = add_stack.size()-1;
		add_stack[last]->SubNodes.push_back(s1);
		add_stack[last]->SubNodes.push_back(s2);
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




int main(int argc, char const *argv[])
{
	//cout<<Add(Sym("A"),Sym("B")).SubNodes[]<<endl;
	//cout<<Add(Sym("A"),Sym("B")).expression<<endl;
	//Node a = Sym("A");Node b = Sym("B");
	//cout<<Add(a,b).show()<<endl;
	//cout<<Sym("B").show()<<endl;
	cout<<add(sym("a"),add(sym("b"),sym("c")) )->expression<<endl;
	return 0;
}