#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <unistd.h>
#include <queue>

using namespace std;

#define MAX_SUB_NODE_NUM 4

/*struct Node
{
	int value;
	int subNodeNum;
	std::vector<Node*> SubNodes; 
};*/

//
//=======================================================================================
//===compare Main_tree and Template_tree if Template_tree is the subtree of Main_tree;===
//=======================================================================================
//
bool HasSameSubTree(Node* RootMain,Node* RootForm)
{
	bool result = false;

	if (RootMain!=NULL && RootForm!=NULL)
	{
		if (RootMain->symbol == RootForm->symbol && RootMain->subNodeNum == RootForm->subNodeNum)
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

//
//===============================================================
//======after finding the same root,compoare their subnodes;=====
//===============================================================
//
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

	if (RootMain.type=="sym" && RootForm.type!="sym")
	{
		return false;
	}

	if (RootForm.type=="sym")
	{
		return true;
	}

	//bool result = true;
	
	//if two nodes are both sym,before this step it has been returned true;
	//if two nodes are both not sym,they have to have the same symbol;(Like num,comput symbol,function...)
	bool result = RootMain.symbol && RootForm.symbol; 
	for (int i = 0; i < RootMain->subNodeNum; ++i)
	{
		result = result && DoseTree1HasTree2(RootMain->SubNodes[i],RootForm->SubNodes[i]);
	}
	return result;
}


//
//================================================================================
//====this is a comprehensive function:just like a reduce process...           ===
//====RootMain   ---(replaceMap)---> RootMain(has been changed)                ===
//====(1)find all sym nodes on template tree using help-stack;                 ===
//====(2)replace the corresponding node on a copy of template tree;            ===
//====(3)move the template tree replaced back into the origin main tree        ===
//================================================================================
//
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


//
//===============================================================
//==== the "i":can show which sub-node should be replaced;   ====
//===============================================================
//
struct ReplaceHelpInfo
{
	Node* node;
	unsigned          i;
};


//
//=============================================================================
//===  the first step:find the sym nodes on ChangedForm(template form);   =====
//=============================================================================
//
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
					continue;//"sym" type node must be leaf node,so...
				}
				findSymOnForm2(ChangedForm->SubNodes[i],HelpStack);
			}
		}
	}
}

//
//===============================================================================================
//=== the second step: make a copy of template tree,and change the corresponding node on it;  ===
//===============================================================================================
//
void changeOnForm2(     const map<Sym,Node*>     replaceMap,
	                                   Node*    ChangedForm,
//	                                   Node* CopyOfTemplate,
	            std::vector<ReplaceHelpInfo>      HelpStack)
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
	//make a copy
	//copy_tree(ChangedForm,CopyOfTemplate);
	for (std::vector<ReplaceHelpInfo>::iterator iter = HelpStack.begin(); iter != HelpStack.end(); ++iter )
	{
		//replace the node on ChangedForm;
		//NOTICE NODE-CHAOS!!!!!!!!!
		//you can only make a new node which's value is same as the want-to-change-node,
		//otherwise you will give that old node onto the CopyOfTemplate tree!!(NC)
		((*iter).node)->SubNodes[(*iter)->i] = replaceMap[ ((*iter).node)->SubNodes[(*iter)->i]->Sym  ];
	}

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


//
//=========================================================================
//=== makeCopyTree:help function,return a tree same as the old one;     ===
//=========================================================================
//
Node* makeCopyTree(Node* originTree)
{
	/*if (originTree!=NULL && originTree->type!="Sym"&& originTree->type!="Num")
	{
		static std::vector<Node*> CopyNodesStack;
		Node* move = originTree;
		if (CopyNodesStack.size()==0) //which means this time it's root node;we need to new a node of root node;
		{
			CopyNodesStack.push_back(new Node( move->type, move->symbol, move->expression));
		}
		//int last = CopyNodesStack.size()-1;
		//start add sub_nodes;
		for (int i = 0; i < originTree->SubNodes.size(); ++i)
		{
			//CopyNodesStack[last]->SubNodes.push_back(new Node(originTree->SubNodes[i]->type,originTree->SubNodes[i]->symbol,originTree->SubNodes[i]->expression));

		}
	}
	if ( originTree->type=="Sym" || originTree->type=="Num")
	{
		CopyNodesStack.push_back(new Node(originTree->type,originTree->symbol,originTree->expression,0));
		return CopyNodesStack[CopyNodesStack.size()-1];
	}
	return NULL;*/

	//first: we do BFS on a tree's nodes into a queue;(and a StaticStack)
	//second: make a empty queue to help reconstruct the copy tree;
	if (originTree==NULL)
	{
		return NULL;
	}
	queue<Node*> firstQueue;
	queue<Node*>  helpQueue;
	static std::vector<Node*> CopyNodesStack;
	Node* move = originTree;

	//BFS
	if(CopyNodesStack.size()==0) //this is root node;
	{
		CopyNodesStack.push_back(new Node(move->type,move->symbol,move->expression,move->subNodeNum));
		firstQueue.push(CopyNodesStack[0]);
	}
	while(!firstQueue.empty())
	{
	    move = firstQueue.front();
	    if (move->subNodeNum==0)
	    {
	    	continue;
	    }
	    for(int i = 0; i < move->subNodeNum; ++i)
	    {
	    	CopyNodesStack.push_back(new Node(move->SubNodes[i]->type,move->SubNodes[i]->symbol,move->SubNodes[i]->expression,move->SubNodes[i]->subNodeNum));
	    	firstQueue.push_back(CopyNodesStack[CopyNodesStack.size()-1]);
	    }
	    firstQueue.pop();
	}    

    //second step:use two queue to link the tree nodes;
    for (int i = 0; i < CopyNodesStack.size(); ++i)
    {
    	firstQueue.push(CopyNodesStack[i]);
    }
    helpQueue.push(firstQueue.front());
    while(!firstQueue.empty())
    {
    	int numOfThisRoot = helpQueue.front()->subNodeNum;
    	while(numOfThisRoot)
    	{
    		helpQueue.front()->SubNodes.push_back(firstQueue->front());
    		helpQueue.push(firstQueue.front());
    		firstQueue.pop();
    		numOfThisRoot--;
    	}
    	helpQueue.pop();
    }
    return CopyNodesStack[0];
}