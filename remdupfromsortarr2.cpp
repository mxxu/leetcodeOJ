#include <iostream>
using namespace std;

class Solution {
public:
    int removeDuplicates(int A[], int n) {
		if (n <= 0)
			return 0;
		int i = 0;
		int j = 1;
		while (j < n) {
			if (A[i] == A[j]) {
				A[++i] = A[j++];
			}
			while (j < n && A[j] == A[i]) j++;
			if (j >= n)
				break;
			A[++i] = A[j++];
		}
		return i+1;
    }
};

int main (int argc, char const *argv[])
{
	Solution sol;
	int A[] = {1,1,1,2,2,3};
	cout << sol.removeDuplicates(A, 6) << endl;
	return 0;
}