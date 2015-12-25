#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
		vector<int> v;
        if (!root) return v;
		
		vector<int> left = inorderTraversal(root->left);
		for (int i = 0; i < left.size(); i++) {
			v.push_back(left[i]);
		}
		v.push_back(root->val);
		vector<int> right = inorderTraversal(root->right);
		for (int i = 0; i < right.size(); i++) {
			v.push_back(right[i]);
		}
		return v;
    }
};

int main (int argc, char const *argv[])
{
	Solution sol;
	TreeNode a(1);
	TreeNode b(2);
	TreeNode c(3);
	TreeNode d(4);
	a.right = &b;
	b.left  = &c;
	vector<int> v = sol.inorderTraversal(&a);
	for (vector<int>::iterator iter = v.begin(); iter != v.end(); iter++) {
		cout << *iter << ",";
	}
	cout << endl;
	return 0;
}