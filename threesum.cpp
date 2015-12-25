#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {
		vector<vector<int> > ret;
		vector<int> x;
		x.push_back(2);
		ret.push_back(x);
        return ret;
    }
};

int main (int argc, char const *argv[])
{
	Solution sol;
	vector<int> num;
	num.push_back(-1);
	num.push_back(0);
	num.push_back(1);
	num.push_back(2);
	num.push_back(-1);
	num.push_back(-4);
	cout << sol.threeSum(num).at(0).at(0) << endl;
	return 0;
}