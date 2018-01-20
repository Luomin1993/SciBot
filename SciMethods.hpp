#include <iostream>
#include <math.h>
#include "SciFormulas.hpp"

using namespace std;

//∇ ∈ ∝ ∧ ∨ ～ ∫ ≠ ≤ ≥ ≈ ∞ π
//α β γ δ ε ζ η θ ι κ λ μ ν
//∈ ∏ ∑ ∕ √ ∝ ∞ ∟ ∠ ∣ ∥ ∧ ∨ ∩ ∪ ∫ ∮ ÷ × ± 
// ∬ ∭ ∯ ∰ ∲ ∂ △ ψ
//º¹²³⁴ⁿ

namespace Methods
{
	void Integral(Formula& Form1,Formula& Form2,Formula& Form3)
	{
		vector<string> paras;
		paras.push_back(Form1.symbol);
		paras.push_back(Form2.symbol);
		Form3.parameters = paras;
		Form3.formula    = "∫("+Form3.parameters[0]+")d("+Form3.parameters[1]+")";
		Form3.expand_formula = "∫("+Form2.expand_formula+")d("+Form2.expand_formula+")";
		Form3.nick       = Form3.symbol+"("+Form1.symbol+","+Form2.symbol+")";
	}


	void quickCreat(string symbol,Formula& Form)
	{
		Form.symbol = symbol;
		Form.nick   = symbol+"(x)";
		Form.expand_formula = "a*x^2+b*x+c";
	}

	void Derivation(Formula& Form1,Formula& Form2)
	{
		Form2.parameters.push_back(Form1.symbol);
		Form2.formula = "∂("+Form2.parameters[0]+")";
		Form2.expand_formula = "∂("+Form1.expand_formula+")";
		Form2.nick    = Form2.symbol+"("+Form1.symbol+")";
	}

	Formula minimize(Formula Form)
	{
		Formula Res;
		Res.symbol  = "Min";
		Res.formula = "∂("+Form.nick+")/θ=0";
		Res.expand_formula = "∂("+Form.formula+")/θ=0";
		Res.nick    = "argmin("+Form.symbol+")";
		return Res;
	}

	Formula optimization(Formula Form)
	{
		Formula Res;
		Res.symbol  = "Min";
		Res.formula = "∂("+Form.formula+")/θ=0";
		Res.nick    = "argmin("+Form.symbol+")";
		Res.expand_formula = "∂("+Form.formula+")/θ=0";
		return Res;
	}

	Formula genetic_optimization(Formula Form)
	{
		Formula Res;
		Res.symbol  = "Min";
		Res.formula = "∂("+Form.formula+")/θ=0";
		Res.nick    = "argmin("+Form.symbol+")";
		Res.expand_formula = "∂("+Form.formula+")/θ=0";
		return Res;
	}
}