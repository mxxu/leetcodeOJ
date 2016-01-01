#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int res = 0;
		for(size_t i = 0; i <= nums.size(); ++i)
		{
			res ^= i;
		}
		for(size_t i = 0; i < nums.size(); ++i)
		{
			res ^= nums[i];
		}
		return res;
    }
};

int main (int argc, char const *argv[])
{
	Solution s;
	std::vector<int> ns;
	ns.push_back(0);
	ns.push_back(1);
	ns.push_back(3);
	cout << s.missingNumber(ns) << endl;
	return 0;
}