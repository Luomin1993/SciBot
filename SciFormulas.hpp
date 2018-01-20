#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

#ifndef SciFormulas
#define SciFormulas


class Formula
{
public:
	Formula();
	Formula(std::vector<string> F_parameters);
	void makeFormula();
	void makeFormula(vector<string> F_parameters);
	void display();
	~Formula();
public:
    string               name;
    int	                   ID;
    string            formula;
    string     expand_formula;
    string           describe;
    vector<string> parameters;
    string             symbol;
    string               nick;

};

#endif