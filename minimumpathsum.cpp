#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int> >& grid) {
		int m = grid.size();
		if (m == 0) return 0;
		int n = grid[0].size();
		if (n == 0) return 0;
		
		std::vector<std::vector<int> > v;
		for(size_t i = 0; i < m; ++i)
		{
			std::vector<int> t;
			for(size_t j = 0; j < n; ++j)
			{
				int value;
				if (i > 0 && j > 0) {
					int up = grid[i][j] + v[i-1][j];
					int left = grid[i][j] + t[j-1];
					value = up;
					if (left < up)
						value = left;
				} else {
					value = grid[i][j];
					if (i > 0)
						value = grid[i][j] + v[i-1][j];
					if (j > 0)
						value = grid[i][j] + t[j-1];
				}
				t.push_back(value);
			}
			v.push_back(t);
		}
        return v[m-1][n-1];
    }
};

int main (int argc, char const *argv[])
{
	Solution s;
	std::vector<std::vector<int> > grid;
	for(size_t i = 0; i < 3; ++i)
	{
		std::vector<int> v;
		for(size_t j = 0; j < 4; ++j)
		{
			v.push_back(j);
		}
		grid.push_back(v);
	}
	cout << s.minPathSum(grid);
	return 0;
}