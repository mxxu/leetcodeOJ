#include <iostream>
using namespace std;

struct TreeLinkNode {
	int val;
    TreeLinkNode *left, *right, *next;
    TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
};

class Solution {
public:
	void _connect(TreeLinkNode *root, TreeLinkNode *right) {
		root->left->next = root->right;
		if (right) {
			root->right->next = right->left;
		} else {
			root->right->next = NULL;
		}
	}
    void connect(TreeLinkNode *root) {
        root->next = NULL;
		_connect(root, NULL);
		_connect(root->left, )
    }
};

int main (int argc, char const *argv[])
{
	Solution sol;
	TreeLinkNode root(1);
	sol.connect(&root);
	return 0;
}