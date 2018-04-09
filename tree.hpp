#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <unistd.h>

using namespace std;

#define MAX_SUB_NODE_NUM 4

/*struct Node
{
	int value;
	int subNodeNum;
	std::vector<Node*> SubNodes; 
};*/

bool HasSameSubTree(Node* RootMain,Node* RootForm)
{
	bool result = false;

	if (RootMain!=NULL && RootForm!=NULL)
	{
		if (RootMain->value == RootForm->value && RootMain->subNodeNum == RootForm->subNodeNum)
		{
			return DoseTree1HasTree2(RootMain,RootForm);
		}
		for (std::vector<Node*>::iterator iter = RootMain->SubNodes.begin(); iter != RootMain->SubNodes.end(); ++ iter)
		{
			result = HasSameSubTree(*iter,RootForm);
			if (result)
			{
				break;
			}
		}
	}

	return result;
}

bool DoseTree1HasTree2(Node* RootMain,Node* RootForm)
{
	if (RootForm == NULL)
	{
		return true;
	}

	if (RootMain->subNodeNum != RootForm->subNodeNum)
	{
		return false;
	}

	if (RootMain == NULL)
	{
		return false;
	}

	
	bool result = true;
	for (int i = 0; i < RootMain->subNodeNum; ++i)
	{
		result = result && DoseTree1HasTree2(RootMain->SubNodes[i],RootForm->SubNodes[i]);
	}
	return result;
}


void changeLikeForm(const map<Sym,Node*> replaceMap,
	                                 Node* RootMain,
	                                 Node*    Start,
	                              Node* ChangedForm)
{
	std::vector<ReplaceHelpInfo> HelpStack;
	findSymOnForm2(ChangedForm,HelpStack);
	//step 1
	changeOnForm2(replaceMap,ChangedForm,HelpStack);
	//step 2
	replaceThatNode(RootMain,Start,ChangedForm);
}

void replaceThatNode(Node* RootMain,
	                 Node*    Start,
	                 Node*   repOne)
{
	if (RootMain==NULL)
	{
		cout<<"ERRROR OF EMPTY TREE"<<endl;
		exit(1);
	}
	if (RootMain->SubNodes.size()!=0)
	{
		for (int i = 0; i < RootMain->SubNodes.size(); ++i)
		{
			if (RootMain->SubNodes[i] == Start)
			{
				RootMain->SubNodes[i] = repOne;
				return;
			}
			replaceThatNode(RootMain->SubNodes[i],Start,repOne);
		}
	}
}	                 


struct ReplaceHelpInfo
{
	Node* node;
	unsigned          i;
};


void findSymOnForm2(Node*              ChangedForm,
	                std::vector<ReplaceHelpInfo>& HelpStack)
{
	if (ChangedForm!=NULL)
	{
		if (ChangedForm->SubNodes.size()>0)
		{
			for (int i = 0; i < ChangedForm->SubNodes.size(); ++i)
			{
				if (ChangedForm->SubNodes[i].type == "Sym")
				{
					HelpStack.push_back(ReplaceHelpInfo(ChangedForm,i));
					continue;
				}
				findSymOnForm2(ChangedForm->SubNodes[i],HelpStack);
			}
		}
	}
}

void changeOnForm2(const map<Sym,Node*> replaceMap,
	                             Node* ChangedForm,
	                 std::vector<ReplaceHelpInfo> HelpStack)
{
	/*if (ChangedForm!=NULL)
	{
		if (ChangedForm->SubNodes.size()!=0)
		{
			for (std::vector<Node*>::iterator iter = ChangedForm->SubNodes.begin(); iter != ChangedForm->SubNodes.end(); ++iter )
			{
				if (*iter!=NULL && *iter->type=="Sym")
				{
					*iter = replaceMap[*iter->value];
				}
			}
		}
	}*/
	for (std::vector<ReplaceHelpInfo>::iterator iter = HelpStack.begin(); iter != HelpStack.end(); ++iter )
	{
		//replace the node on ChangedForm;
		((*iter).node)->SubNodes[(*iter)->i] = replaceMap[ ((*iter).node)->SubNodes[(*iter)->i]->Sym  ];
	}

}	               