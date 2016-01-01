#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
		if (n == 1) return 0;
		if (nums[0] > nums[1]) return 0;
		if (nums[n-1] > nums[n-2]) return n-1;
		int l = 1, r = n-2, mid;
		while (l < r) {
			mid = l + (r - l)/2;
			if (nums[mid] > nums[mid-1] && nums[mid] > nums[mid + 1]) {
				return mid;
			} else if (nums[mid] > nums[mid-1] && nums[mid] < nums[mid+1]) {
				l = mid + 1;
			} else if (nums[mid] > nums[mid+1] && nums[mid] < nums[mid-1]) {
				r = mid - 1;
			} else {
				l = mid + 1;
			}
		}
		return l;
    }
};

int main (int argc, char const *argv[])
{
	Solution s;
	std::vector<int> n;
	n.push_back(3);
	n.push_back(4);
	n.push_back(3);
//	n.push_back(1);
	n.push_back(2);
	n.push_back(1);
	cout << s.findPeakElement(n);
	return 0;
}