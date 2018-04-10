#include <iostream>
#include <map>
#include <vector>

using namespace std;

struct treeNode
{
	int value;
	treeNode* left  = NULL;
	treeNode* right = NULL;
	treeNode(int val){value = val;}
};


/*
           1
         /  \
        2    3
       / \  / \
      4  5 6  7
*/
treeNode* make_tree()
{
	static std::vector<treeNode*> vec;
	for (int i = 1; i < 8; ++i)
	{
		vec.push_back(new treeNode(i));
	}
	vec[0]->left = vec[1];vec[0]->right = vec[2];
	vec[1]->left = vec[3];vec[1]->right = vec[4];
	vec[2]->left = vec[5];vec[2]->right = vec[6];
	return vec[0];
}

void traversing_tree_mid(treeNode* root)
{
	if (root)
	{
		traversing_tree_mid(root->left);
		cout<<root->value<<endl;
		traversing_tree_mid(root->right);
	}
}

void traversing_tree_after(treeNode* root)
{
	if (root)
	{
		traversing_tree_after(root->left);
		traversing_tree_after(root->right);
		cout<<root->value<<endl;
	}
}


int main(int argc, char const *argv[])
{
	//traversing_tree_mid(make_tree());
	traversing_tree_after(make_tree());
	return 0;
}