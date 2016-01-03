#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        std::vector<int> v;
		int n = nums.size();
		v.push_back(nums[1]);
		v.push_back(nums[0]);
		for(size_t i = 2; i < n; ++i)
		{
			v
		}
		return v;
    }
};

int main (int argc, char const *argv[])
{
	Solution s;
	std::vector<int> v;
	v.push_back(1);
	v.push_back(2);
	v.push_back(3);
	v.push_back(4);
	cout << s.productExceptSelf(v);
	return 0;
}