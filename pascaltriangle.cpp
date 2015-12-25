class Solution {
public:
    vector<vector<int> > generate(int numRows) {
        vector<vector<int> > triangles;
		for (int i = 0; i < numRows; i++) {
			if (i == 0) {
				vector<int> v;
				v.push_back(1);
				triangles.push_back(v);
			} else {
				int n = i + 1;
				vector<int> v;
				vector<int> last = triangles.back();
				for (int j = 0; j < n; j++) {
					if (j == 0 || j == n - 1)
						v.push_back(1);
					else
						v.push_back(last[j-1] + last[j]);
				}
				triangles.push_back(v);
			}
		}
		return triangles;
    }
};