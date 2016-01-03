#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
		int n = ratings.size();
		std::vector<int> v(n, 0);
		v[0] = 1;
		for(int i = 1; i < n; ++i)
		{
			if (ratings[i] > ratings[i-1])
				v[i] = v[i-1] + 1;
			else if (ratings[i] < ratings[i-1])
				v[i] = 1;
			else
				v[i] = 1;
			if (v[i] <= 0)
				v[i] = 1;
		}
		for(int i = n-2; i >= 0; --i)
		{
			if (ratings[i] > ratings[i+1]) {
				if (v[i] <= v[i+1])
					v[i] = v[i+1] + 1;
			}
			else if (ratings[i] < ratings[i+1]) {
				if (v[i] >= v[i+1])
					v[i] = v[i+1] - 1;
			}
			else {
				if (v[i] < 1)
					v[i] = 1;
			}
		}
		int ret = 0;
		for(size_t j = 0; j < v.size(); ++j)
		{
			cout << v[j] << ",";
			ret += v[j];
		}
		cout << endl;
        return ret;
    }
};

int main (int argc, char const *argv[])
{
	Solution s;
//	int ratings[] = {1,2,3,2,1,0,-1,0,1,2,3,4,5,4,3};
	int ratings[] = {1,2,2};
	std::vector<int> v(ratings, ratings+sizeof(ratings)/sizeof(int));
	cout << s.candy(v);
	return 0;
}