#include "../tree.hpp"
#include <iostream>

using namespace std;


main(int argc, char const *argv[])
{
	Node* tree = equal(sym("a") , devide(sym("b"),sym("c")));
	cout<<makeCopyTree(tree)->expression<<endl;
	return 0;
}