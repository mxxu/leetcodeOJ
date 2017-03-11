#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        int maxArea(vector<int>& height) {
            int ret = 0;
            int i = 0, j = height.size() - 1;
            while (i < j) {
                int shorter = i;
                if (height[j] < height[i])
                    shorter = j;

                int area = (j - i) * height[shorter];
                if (ret < area)
                    ret = area;

                if (shorter == i)
                    ++i;
                else
                    --j;
            }
            return ret;
        }
};

int main(int argc, char *argv[]) {
    Solution s;
    vector<int> v;
    v.push_back(1);
    v.push_back(5);
    v.push_back(2);
    v.push_back(4);
    v.push_back(3);
    v.push_back(3);
    cout << s.maxArea(v) << endl;
    return 0;
}
