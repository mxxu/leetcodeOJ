#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
		vector<vector<int> > ret;
        if (!root) return ret;
		if (!root->left && !root->right) {
			if (root->val == sum) {
				vector<int> v;
				v.push_back(root->val);
				ret.push_back(v);
				return ret;
			} else return ret;
		}
		int subsum = sum - root->val;
		if (root->left) {
			vector<vector<int> > result = pathSum(root->left, subsum);
			if (result.size() > 0) {
				
			}
		}
    }
};