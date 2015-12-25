#include <iostream>
using namespace std;

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
		int m = s1.size(), n = s2.size();
		if (m + n != s3.size()) return false;
		
		int p[100][100];
		/*
		int **p =new int*[m+1];

		for(int i=0;i<m+1;i++)
		    p[i] = new int[n+1];
		*/
		for(int i=0;i<m+1;i++)
		  	for(int j=0;j<n+1;j++)
				p[i][j]=0;
		
		p[0][0] = 1;
		for (int k = 0; k < m + n; k++) {
			bool found = false;
			for (int i = 0; i <= m && i <= k+1; i++) {
				int j = k + 1 - i;
				if (i > 0 && s1[i-1] == s3[k] && p[i-1][j] == 1) {
					found = true;
					p[i][j] = 1;
				}
				if (j > 0 && s2[j-1] == s3[k] && p[i][j-1] == 1) {
					found = true;
					p[i][j] = 1;
				}
				//cout << i << "," << j << ":" << p[i][j] << endl;
			}
			if (!found) {
				break;
			}
		}
		
		bool ret = p[m][n] == 1;

		/*
		for(int i=0;i<m+1;i++) delete []p[i];
		delete []p;
		*/
		return ret;
    }
};

int main (int argc, char const *argv[])
{
	Solution sol;
	cout << sol.isInterleave("bcacbaacbaabaacacbcccb", "bbaacbbcbcbcbacbbbcbaaba", "bbbcaaacbcabbcabcbaaabbcaccaacbacbcbbcccbbbaba") << endl;
	return 0;
}