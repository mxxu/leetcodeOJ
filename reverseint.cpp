#include <iostream>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        long l = 0;
		bool neg = false;
		if (x < 0) {
			neg = true;
			x = 0 - x;
		}
		
		while (x > 0) {
			int n = x % 10;
			l = l * 10 + n;
			x = x / 10;
		}
		if (neg)
			l = 0 - l;
		if ((l > 0 && l > std::numeric_limits<int>::max()) ||
			(l < 0 && l < std::numeric_limits<int>::min()))
			return 0;
		return int(l);
    }
};

int main (int argc, char const *argv[])
{
	/* code */
	Solution s;
	cout << s.reverse(1000000003) << endl;
	return 0;
}