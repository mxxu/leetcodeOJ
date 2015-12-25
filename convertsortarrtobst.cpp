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
    TreeNode *sortedArrayToBST(vector<int> &num) {
		return _sortedArrayToBST(num, 0, num.size());
	}
	
    TreeNode *_sortedArrayToBST(vector<int> &num, int begin, int n) {
		if (n <= 0 || begin >= num.size()) return NULL;
		if (n == 1) {
			TreeNode *node = new TreeNode(num[begin]);
			return node;
		}
		int mid = begin + n/2;
		TreeNode *root = new TreeNode(num[mid]);
		root->left = _sortedArrayToBST(num, begin, mid-begin);
		root->right = _sortedArrayToBST(num, mid+1, begin+n-mid-1);
		return root;
    }
};

void printTree(TreeNode *root) {
	if (!root) return;
	
	printTree(root->left);
	cout << root->val << ",";
	printTree(root->right);
}

int main (int argc, char const *argv[])
{
	Solution sol;
	vector<int> num;
	num.push_back(-1);
	num.push_back(0);
	num.push_back(1);
	num.push_back(2);
	TreeNode *root = sol.sortedArrayToBST(num);
	printTree(root);
	return 0;
}