#include <iostream>

using namespace std;

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSameTree(TreeNode *p, TreeNode *q) {
		if (p == NULL && q == NULL)
			return true;
		if (p == NULL && q != NULL || p != NULL && q == NULL)
			return false;
        if (p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right))
			return true;
		return false;
    }
};

int main (int argc, char const *argv[])
{
	Solution sol;
	sol.isSameTree(p, q);
	return 0;
}