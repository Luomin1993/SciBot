#include "SciFormulas.hpp"

Formula::Formula(){}
Formula::~Formula(){}

void Formula::display()
{
	cout<<symbol<<" = "<<nick<<endl;
	cout<<"  = "<<formula<<endl;
	cout<<"  = "<<expand_formula<<endl;
	cout<<" "<<endl;
}

/*
Formula models_1D()
{
   //models_1D
   Formula models_1D;
   models_1D.formula = "△ X/ε";
   models_1D.symbol = "g";
   models_1D.nick   = "g(△ X,ε)";
   return models_1D;
}

Formula models_3D()
{
   //models_3D
   Formula models_3D;
   models_3D.formula = "∑(△ Xi/ε)";
   models_3D.symbol = "g";
   models_3D.nick   = "g(△ Xi,ε)";
   return models_3D;
}

Formula objective_function()
{
   //objective_function
   Formula objective_function;
   objective_function.formula = "(Wq0-Wq)/ε² + ∑(△ W²/ε²) + ∑(△ ψ²/ε²) + ∑(△ α²/ε²) + ∑β";
   objective_function.symbol = "F";
   objective_function.nick   = "F(△ W,△ ψ,△ α,ε)";
   return objective_function;
}

Formula TRACK()
{
    //TRACK
	Formula TRACK;
	TRACK.formula = "A*C+B";
	TRACK.symbol  = "M";
	TRACK.nick    = "M(C)";
	return TRACK;
}*/