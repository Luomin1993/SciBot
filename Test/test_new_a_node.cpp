#include <map>
#include <vector>
#include <iostream>

using namespace std;

struct Node
{
	int value;
	Node* next;
	Node(int val){value = val;}
};

void print_chain(Node* chain)
{
	Node* move = chain;
	while(move)
	{
		cout<<move->value<<endl;
		move = move->next;
	}
}

Node* new_chain_and_change(Node* chain)
{
	static Node* new_chain = chain;
	static Node* new_node;
	//new_node->value = 99;
	new_node = new Node(99);
	(new_chain->next)->next = new_node;
	return new_chain;
}



Node* make_copy( Node* chain)
{
	Node* move = chain;
	static std::vector<Node*> vec;
	int i = 0;
	while(move)
	{
		vec.push_back(new Node(move->value));
		if (i>0)
		{
			vec[i-1]->next = vec[i];
		}
		i++;
		move = move->next;
	} 
	return vec[0];
}

Node Test_make_copy(Node* chain)
{
	Node* copy_chain = make_copy(chain);
	print_chain(copy_chain);
	cout<<" "<<endl;
	copy_chain->next = new Node(33);
	copy_chain->next->next = NULL;
	print_chain(chain);
	cout<<" "<<endl;
	print_chain(copy_chain);
}

Node* make_chain(std::vector<int> value_vec)
{
	//static Node* chain;
	//static Node* temp;
	static vector<Node*> dynamic_nodes;
	for(int i = 0; i < value_vec.size(); ++i)
	{
		/*if (i==0)
		{
			//chain->value = value_vec[i];
			chain = new Node(value_vec[i]);
			chain->next  = temp;
			continue;
		}*/
		dynamic_nodes.push_back(new Node(value_vec[i]));
		if (i>0)
		{
			dynamic_nodes[i-1]->next = dynamic_nodes[i];
		}
	}
	//return chain;
	return dynamic_nodes[0];
}

int main(int argc, char const *argv[])
{
	std::vector<int> value_vec;
	value_vec.push_back(1);value_vec.push_back(2);value_vec.push_back(3);value_vec.push_back(4);value_vec.push_back(5);
	Node* chain = make_chain(value_vec);
	//print_chain(chain);
	//Node* new_chain = new_chain_and_change(chain);
	//print_chain(new_chain);
	Test_make_copy(chain);
	return 0;
}