#include <iostream>

using namespace std;

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	bool isSymmetricSub(TreeNode* a, TreeNode* b) {
		if (!a && !b) return true;
		if (a && !b || !a && b) return false;
		if (a->val != b->val) return false;
		return isSymmetricSub(a->left, b->right) && isSymmetricSub(a->right, b->left);
	}
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
		if (!root->left && !root->right) return true;
		return isSymmetricSub(root->left, root->right);
    }
};

int main (int argc, char const *argv[])
{
	TreeNode root = TreeNode(1);
	TreeNode x = TreeNode(2);
	TreeNode y = TreeNode(2);
	TreeNode z = TreeNode(3);
	TreeNode p = TreeNode(3);
	TreeNode q = TreeNode(4);
	TreeNode r = TreeNode(4);
	root.left = &x;
	root.right = &y;
	root.left->left = &z;
	root.right->right = &p;
	root.left->right = &q;
	root.right->left = &r;
	Solution s;
	cout << s.isSymmetric(&root) << endl;
	return 0;
}