#include <iostream>

using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        int ret = 0;
		
		size_t i = 0;
		size_t n = str.size();
		if (n == 0)
			return 0;
		while (i < n && str[i] == ' ')
			++i;
		
		if (i == n)
			return 0;
		
		bool neg = false;
		if (str[i] == '-') {
			neg = true;
			++i;
		} else if (str[i] == '+') {
			++i;
		}
		
		while (str[i] >= '0' && str[i] <= '9') {
			int tmp = ret;
			ret = ret * 10 + str[i] - '0';
			if (ret < 0 || (ret - (str[i] - '0'))/10 != tmp) {
				if (!neg)
					return std::numeric_limits<int>::max();
				else
					return std::numeric_limits<int>::min();
			}
			i++;
		}
		if (neg)
			ret = 0 - ret;
		
		return ret;
    }
};

int main (int argc, char const *argv[])
{
	/* code */
	Solution s;
	cout << s.myAtoi("  -12345123450") << endl;
	return 0;
}