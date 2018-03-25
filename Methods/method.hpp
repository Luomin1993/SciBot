#include <iostream>
#include <vector>
#include <map>

struct parameters
{
	int num;
	vector<string> paras;
};

class method
{
public:
	method();
	~method();
	void print_formula();
	void   get_formula();
public:
	string                name;
	string              symbol;
    parameters           paras;	
    parameters         results;
    parameters   default_paras;
    parameters default_results;
};