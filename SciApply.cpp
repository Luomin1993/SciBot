#include "SciMethods.hpp"
#include "KnownFormulas.hpp"
#include <map>

typedef map<string,Formula(*)(Formula)> MethodsMap;
typedef map<string,Formula(*)(void)> FormulasMap;

//g++ SciApply.cpp SciFormulas.cpp -o exe -std=c++11

using namespace Methods;
using namespace std;




void showApply(Formula (*func)(Formula Form),Formula (*makeForm)(void))
{
	Formula Res = func(makeForm());
	Res.display();
}

int main(int argc, char const *argv[])
{
    //-------------------------------------------------
	MethodsMap methods_map;
	methods_map["minimize"]             = minimize;
	methods_map["optimization"]         = optimization;
	methods_map["genetic_optimization"] = genetic_optimization;
    //-------------------------------------------------

    //-------------------------------------------------
	FormulasMap formulas_map;
	formulas_map["models_1D"] = models_1D;
	formulas_map["models_3D"] = models_3D;
	formulas_map["objective_function"] = objective_function;
	formulas_map["TRACK"] = TRACK;
    //-------------------------------------------------


	string Method  = argv[1];
	string Formula = argv[2];
	if(methods_map.find(Method)!=methods_map.end() && formulas_map.find(Formula)!=formulas_map.end())
	{
		showApply(methods_map[Method],formulas_map[Formula]);
	}
	return 0;
}