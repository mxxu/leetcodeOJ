#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string removeDuplicateLetters(string s) {
        int loc[26];
		for(size_t i = 0; i < 26; ++i)
		{
			loc[i] = -1;
		}
		std::vector<char> v;
		for(int i = s.size()-1; i >= 0; --i)
		{
			char c = s[i];
			int locidx = c - 'a';
			if (loc[locidx] == -1) {
				loc[locidx] = i;
				v.insert(v.begin(), c);
			} else {
				if (v[0] > c) {
					loc[locidx] = i;
					v.insert(v.begin(), c);
				}
			}
		}
		
		string ret;
		for(size_t i = 0; i < v.size(); ++i)
		{
			char c = v[i];
			if (loc[c - 'a'] >= 0) {
				ret.push_back(c);
				loc[c - 'a'] = -1;
			}
		}
		return ret;
    }
};

int main(int argc, const char *argv[]) {
	Solution s;
	string s2 = s.removeDuplicateLetters("cbacdcbc");
	cout << s2 << endl;
	return 0;
}