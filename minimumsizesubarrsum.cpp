#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
		int n = nums.size();
		if (n == 0) return 0;
		int i = 0, j = 0;
		int min_size = n+1;
		int subsum = nums[0];
		while (i < n && j < n) {
			if (subsum >= s) {
				int curr_size = j - i + 1;
				if (curr_size == 1) return 1;
				if (min_size > curr_size)
					min_size = curr_size;
				subsum -= nums[i];
				i++;
				if (i > j) {
					j++;
					if (j >= n)
						break;
					subsum += nums[j];
				}
			} else {
				j++;
				if (j >= n)
					break;
				subsum += nums[j];
			}
		}
		if (min_size <= n)
			return min_size;
        return 0;
    }
};

int main (int argc, char const *argv[])
{
	Solution s;
	std::vector<int> v;
	v.push_back(2);
	v.push_back(3);
	v.push_back(1);
	v.push_back(2);
	v.push_back(4);
	v.push_back(3);
	cout << s.minSubArrayLen(7, v);
	return 0;
}