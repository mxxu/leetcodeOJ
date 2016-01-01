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
    int maxPathSum(TreeNode* root) {
        if (!root)
			return 0;
		int ms = root->val;
		
		bool l = false, r = false;
		int ls, rs;
		if (root->left) {
			ls = maxPathSum(root->left);
			if (ls > ms)
				ms = ls;
			if (ls + root->val > ms)
				ms = ls + root->val;
			l = true;
		}
		if (root->right) {
			rs = maxPathSum(root->right);
			if (rs > ms)
				ms = rs;
			if (rs + root->val > ms)
				ms = rs + root->val;
			r = true;
		}
		if (l && r && ls + rs + root->val > ms)
			ms = ls + rs + root->val;
		
		return ms;
    }
};

int main (int argc, char const *argv[])
{
	Solution s;
	TreeNode root(1), l(2), r(3);
	root.left = &l;
	root.right = &r;
	cout << s.maxPathSum(&root);
	r.val = -3;
	cout << s.maxPathSum(&r);
	root.val = 0;
	l.val = 1;
	r.val = 1;
	cout << s.maxPathSum(&root);
	return 0;
}