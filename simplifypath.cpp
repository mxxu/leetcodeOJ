#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
		int n = path.size();
		int i = 0;
		while (i < n && path[i] != '/') i++;
		if (i == n)
			return "";
		std::vector<string> v;
		while (i < n-1)
		{
			int j = i+1;
			while (j < n && path[j] != '/') j++;
			string sub = path.substr(i+1, j-i-1);
			if (sub == "." || sub == "") {
				i = j;
				continue;
			} else if (sub == "..") {
				if (v.size() > 0)
					v.pop_back();
			} else {
				v.push_back(sub);
			}
			i = j;
		}
		if (v.size() == 0)
			return "/";
		
		string ret;
		for(size_t i = 0; i < v.size(); ++i)
		{
			ret.append("/" + v[i]);
		}
        return ret;
    }
};

int main (int argc, char const *argv[])
{
	Solution s;
	string p("/home//foo");
	cout << s.simplifyPath(p);
	return 0;
}