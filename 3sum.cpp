#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {
		vector<vector<int> > ret;
		if (num.size() < 3) return ret;
		sort(num.begin(), num.end());
		if (num.size() == 3) {
			if (num[0] + num[1] + num[2] == 0) {
				ret.push_back(num);
			}
			return ret;
		}
		
		if (num.front() > 0 || num.back() < 0) return ret;
		/*
		for (int i : num) {
			cout << i << ",";
		}*/
		for (int i = 0; i < num.size(); i++) {
			if (num[i] > 0)
				break;
			int j = i+1;
			int k = num.size() - 1;
			
			bool found = false;
			while (j < k) {
				int sum = num[i] + num[j] + num[k];
				if (sum > 0) k--;
				else if (sum < 0) j++;
				else {
					found = true;
					if (ret.size() > 0) {
						vector<int> last = ret.back();
					}
					break;
				}
			}
			
			if (found) {
				bool dup = false;
				if (ret.size() > 0) {
					vector<int> last = ret.back();
					if (last[0] == num[i] && last[1] == num[j] && last[2] == num[k])
						dup = true;
				}
				if (!dup) {
					vector<int> tmp;
					tmp.push_back(num[i]);
					tmp.push_back(num[j]);
					tmp.push_back(num[k]);
					ret.push_back(tmp);
				}
			}
		}
		return ret;
    }
};

int main (int argc, char const *argv[])
{
	Solution sol;
	vector<int> num;
	num.push_back(-2);
	num.push_back(0);
	num.push_back(1);
	num.push_back(1);
	num.push_back(2);
	vector<vector<int> > ret = sol.threeSum(num);
	for (vector<int> v : ret) {
		for (int i : v) {
			cout << i << " ";
		}
		cout << endl;
	}
	return 0;
}