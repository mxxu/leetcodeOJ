#include <iostream>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
		if (x < 10) return true;
		if (x % 10 == 0) return false;
		int y = 0, ox = x;
		while (x > 0) {
			y = y * 10 + x % 10;
			x = x / 10;
		}
		return ox == y;
    }
};

int main (int argc, char const *argv[])
{
	Solution s;
	cout << s.isPalindrome(111);
	return 0;
}