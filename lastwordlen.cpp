#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(const char *s) {
		bool hasSpace = false;
        while (s) {
			cout << *s << endl;
        	if (*s == ' ')
				hasSpace = true;
			s++;
        }
		return 1;
    }
};

int main (int argc, char const *argv[])
{
	Solution sol;
	char s[] = "asdf";
	cout << sol.lengthOfLastWord(s);
	return 0;
}