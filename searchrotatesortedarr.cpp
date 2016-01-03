#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
		int n = nums.size();
		if (n == 0) return -1;
		int left = 0, right = n-1, mid;
		while (left <= right) {
			mid = left + (right - left)/2;
			if (nums[mid] == target) return mid;
			if (nums[mid] > nums[right]) {
				if (target > nums[left] && target < nums[mid])
					right = mid - 1;
				else
					left = mid + 1;
			} else {
				if (target > nums[mid] && target < nums[right])
					left = mid + 1;
				else
					right = mid - 1;
			}
		}
    	return -1;
    }
};

int main (int argc, char const *argv[])
{
	Solution s;
	//int nums[] = {4,5,6,7,0,1,2};
	int nums[] = {3,1};
	std::vector<int> v(nums, nums+sizeof(nums)/sizeof(int));
	cout << s.search(v, 1);
	return 0;
}