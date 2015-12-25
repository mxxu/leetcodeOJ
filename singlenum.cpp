#include <iostream>
using namespace std;

class Solution {
public:
    int singleNumber(int A[], int n) {
		int ret = 0;
		for (int i = 0; i < n; i++) {
			ret = ret ^ A[i];
		}
        return ret;
    }
};

int main (int argc, char const *argv[])
{
	Solution sol;
	int A[] = {1,2,2,3,1};
	cout << sol.singleNumber(A, 5) << endl;
	return 0;
}