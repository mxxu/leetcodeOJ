#include <iostream>

using namespace std;

class Solution {
public:
    string convertToTitle(int n) {
		string s;
		while (n > 0) {
			int left = (n-1)%26;
			s.insert(0, 1, 'A' + left);
			n = (n-1)/26;
		}
		return s;
    }
};

int main (int argc, char const *argv[])
{
	Solution s;
	cout << s.convertToTitle(2147483647);
	return 0;
}