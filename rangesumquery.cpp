#include <iostream>

using namespace std;

class NumArray {
public:
    NumArray(vector<int> &nums) {
        
    }

    void update(int i, int val) {
        
    }

    int sumRange(int i, int j) {
        
    }
};


// Your NumArray object will be instantiated and called as such:
// NumArray numArray(nums);
// numArray.sumRange(0, 1);
// numArray.update(1, 10);
// numArray.sumRange(1, 2);

int main (int argc, char const *argv[])
{
	NumArray numArray(nums);
	cout << numArray.sumRange(0, 1) << endl;
	numArray.update(1, 10);
	cout << numArray.sumRange(1, 2);
	return 0;
}