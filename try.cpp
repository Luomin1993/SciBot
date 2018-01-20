#include <iostream>
#include <math.h>
#include <functional>
#include <vector>
#include <map>
#include "SciMethods.hpp"
//g++ try.cpp SciFormulas.cpp -o exe -std=c++11

using namespace std;

//∇ ∈ ∝ ∧ ∨ ～ ∫ ≠ ≤ ≥ ≈ ∞ π
//α β γ δ ε ζ η θ ι κ λ μ ν
//∈ ∏ ∑ ∕ √ ∝ ∞ ∟ ∠ ∣ ∥ ∧ ∨ ∩ ∪ ∫ ∮ ÷ × ± 

float SIN(float x)
{
	return sin(x);
}

template <typename operation, typename T> 
operation derivative_any(operation f, T dx) {
    return [=](T x)->T {
        return (f(x + dx) - f(x)) / dx;
    };
}


/*int main(int argc, char const *argv[])
{
	//cout<<(derivative_any<float (*)(float),float>(SIN,0.01))(1.0)<<endl;
	return 0;
}*/

//motherfucker!!
//I can transfer this func into another f() but I can only write this func as "lambda".
//It's not flexible;
double eval(std::function<double(double)> f, double x = 2.0)
{
    return f(x);
}

/*int main()
{
    map<string,std::function<void(void)> > FuncMap;
    std::function<void(void)> Sin1  = [](){cout<<SIN(0.01)<<endl;};
    std::function<void(void)> Sin2  = [](){cout<<SIN(3.14)<<endl;};
    FuncMap["f1"] = Sin1;
    FuncMap["f2"] = Sin2;
    //FuncMap["f1"]();
    //FuncMap["f2"]();
    cout<<"∑Xi"<<endl;
    return 0;
}*/

int main(int argc, char const *argv[])
{
	Formula f1,f2,f3;
	Methods::quickCreat("f1",f1);
	Methods::quickCreat("f2",f2);
	f3.symbol = "F";
	Methods::Integral(f1,f2,f3);
	f3.display();
	Methods::Derivation(f1,f3);
	f3.display();
	return 0;
}