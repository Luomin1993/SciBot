#include <iostream>
#include <vector>
#include <map>

using namespace std;

class compute_symbol
{
public:
    compute_symbol();
    ~compute_symbol();
    void printFormula();
    string giveFormula();
    void setParas();
public:
    string symbol;
    int    para_num;
    vector<string> paras;
};

class sqrt_symbol:compute_symbol
{
public:
    sqrt_symbol()
    {
        symbol = "√";
        paras.push_back("x");
        para_num = paras.size();
    }

    void printFormula()
    {
        cout<<giveFormula()<<endl;
    }    

    string giveFormula()
    {
        return "√(" + paras[0] + ")";
    }
};




class integral:compute_symbol
{
public:
    integral()
    {
        symbol = "∲d";
        paras.push_back("f(x)");
        paras.push_back("x");
        para_num = paras.size();
    }

    void printFormula()
    {
        cout<<giveFormula()<<endl;
    }    

    string giveFormula()
    {
        return "∲(" + paras[0] + ")" + "d" + paras[1];
    }
};



struct symbol_node
{
    compute_symbol cs;
    int paras_num;
    bool is_leaf;
    string leaf_symbol;
    vector<symbol_node*> sons;
};


//--example--: Fi( Div(Sym("x",), Sqrt(Dot(Sym("2"),Dot(Sym("m"),Sub(Sym("E"),Sym("U"))))) ), Sym("x"));
//symbol_node* make(){}


class method
{
public:
    method(){};
    //~method();
    //string giveResult();
public:
    string (*giveResult)(vector<string> paras);
    vector<string> paras;
    vector<string> results;    
};





string Energy(vector<string> paras)
{
    if (paras.size()==0)
    {
        return "mv²/2+U"; 
    }
    return paras[0] + paras[1] + "²/2" + "+" + paras[2];
}

string Jene(vector<string> paras)
{
    if (paras.size()==0)
    {
        return "∲√(2m(E-U))dx";
    }
    return "∲" + paras[0] + "d" + paras[1];
}

string Derivation(vector<string> paras)
{
    if (paras.size()==0)
    {
        return "∂F/∂x";
    }
    if (paras.size()==1)
    {
        return "∂(" + paras[0] + ")/∂x";
    }
    return "∂(" + paras[0] + ")/∂(" + paras[1] +")";
}

string inverse(vector<string> paras)
{
    if (paras.size()==0)
    {
        return "1/x";
    }
    return "1/(" + paras[0] + ")";     
}

method broker(method m1,method m2,string relationship)
{
    method res;
    if( relationship=="parallel")
    {
        res.results.push_back(m1.giveResult(vector<string>() ));
        res.results.push_back(m2.giveResult(vector<string>() ));
        return res;
    }
    if( relationship=="serialize")
    {
        m2.paras = m1.results;
        res.results.push_back(m2.giveResult(m2.paras));
        return res;
    }
    //case "recurrent":
    return res;
}

method broker(method m,string relationship)
{
	//method res;
	if (relationship=="recurrent")
	{
		if (m.paras.size()==0)
		{
			m.paras.push_back(m.giveResult(m.paras));
			return m;
		}
		m.paras[0] = m.giveResult(m.paras);
		//m.results.push_back(m.giveResult(m.paras));
		return m;
	}
	return m;
}

void split(const string& s, vector<string>& v, const string& c)
{
    string::size_type pos1, pos2;
    pos2 = s.find(c);
    pos1 = 0;
    while(string::npos != pos2)
    {
        v.push_back(s.substr(pos1, pos2-pos1));
         
        pos1 = pos2 + c.size();
        pos2 = s.find(c, pos1);
    }
    if(pos1 != s.length())
        v.push_back(s.substr(pos1));
}



int main(int argc, char const *argv[])
{
    /* code */
    method E;E.giveResult = Energy;
    method J;J.giveResult = Jene;
    method D;D.giveResult = Derivation;
    method iv;iv.giveResult = inverse;
    //cout<<broker(E,J,"parallel").results[0]<<endl;
    map<string,method> MethodsMap;
    MethodsMap["energy"] = E;
    MethodsMap["jene"]   = J;
    MethodsMap["derivation"] = D;
    MethodsMap["inverse"]    = iv;

    string text = "We let the energy and the jene to do the derivation,and it's inverse is the frequence;";
    vector<string> a;
    split(text,a," ");
    for(int i=0;i<a.size();i++)
    {cout<<a[i]<<endl;}
    

    cout<<" "<<endl;
    cout<<"f = "<<broker(broker(broker(E,J,"parallel"),D,"serialize"),iv,"serialize").results[0]<<endl;

    cout<<"f = "<<broker(broker(D,"recurrent"),"recurrent").paras[0]<<endl;
    return 0;
}