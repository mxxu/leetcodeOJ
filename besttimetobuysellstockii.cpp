#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &prices) {
		int maxprofit = 0;
		int i = 0;
		int n = prices.size();
		while (i < n) {
			int start = i;
			while (i < n-1 && prices[i+1] >= prices[i]) i++;
			if (start < i) {
				maxprofit += prices[i] - prices[start];
			}
			if (i == n - 1) break;
			while (i < n-1 && prices[i+1] < prices[i]) i++;
		}
		return maxprofit;
    }
};

int main (int argc, char const *argv[])
{
	/* code */
	vector<int> v;
	v.push_back(1);
	v.push_back(2);
	v.push_back(3);
	v.push_back(2);
	v.push_back(5);
	Solution sol;
	cout << sol.maxProfit(v) << endl;
	return 0;
}