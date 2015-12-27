#include <iostream>
#include <map>

using namespace std;

class Solution {
public:
    bool wordPattern(string pattern, string str) {
        std::map<string, char> map;
		std::map<char, string> cmap;
		
		size_t pos = 0;
		for(size_t i = 0; i < pattern.size(); ++i)
		{
			if (pos >= str.size())
				return false;
			string word;
			size_t end = str.find_first_of(' ', pos);
			if (end == string::npos) {
				word = str.substr(pos, str.size() - pos);
				pos = str.size();
			} else {
				word = str.substr(pos, end-pos);
				pos = end + 1;
			}
			char c = pattern[i];
			if (map.find(word) != map.end()) {
				if (map[word] != c) {
					return false;
				}
			} else {
				map[word] = c;
			}
			
			if (cmap.find(c) != cmap.end()) {
				if (cmap[c] != word) {
					return false;
				}
			} else {
				cmap[c] = word;
			}
		}
		if (pos != str.size())
			return false;
		return true;
    }
};


int main(int argc, const char *argv[]) {
	Solution s;
	bool b = s.wordPattern("aaa", "aa aa aa aa");
	cout << b << endl;
	return 0;
}