#include <vector>
#include <iostream>
using namespace std;

struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};

class Solution {
public:
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
        vector<Interval> ret;
		if (intervals.size() == 0) {
			ret.push_back(newInterval);
			return ret;
		}
		for (int i = 0; i < intervals.size(); i++) {
			Interval &interval = intervals[i];
			if (interval.end < newInterval.start) {
				ret.push_back(interval);
				if (i == intervals.size() - 1) {
					ret.push_back(newInterval);
					return ret;
				}
				continue;
			}
			
			if (interval.start > newInterval.end) {
				ret.push_back(newInterval);
				for (int j = i; j < intervals.size(); j++) {
					ret.push_back(intervals[j]);
				}
				return ret;
			}
			
			Interval genInterval;
			genInterval.start = newInterval.start;
			if (newInterval.start > interval.start) genInterval.start = interval.start;
			genInterval.end = interval.end;
			if (interval.end < newInterval.end) {
				bool stop = false;
				for (int k = i+1; k < intervals.size(); k++) {
					if (stop) {
						ret.push_back(intervals[k]);
						continue;
					}
					if (newInterval.end < intervals[k].start) {
						genInterval.end = newInterval.end;
						ret.push_back(genInterval);
						ret.push_back(intervals[k]);
						stop = true;
					} else if (newInterval.end < intervals[k].end) {
						genInterval.end = intervals[k].end;
						ret.push_back(genInterval);
						stop = true;
					}
				}
				if (!stop) {
					genInterval.end = newInterval.end;
					ret.push_back(genInterval);
				}
			} else {
				ret.push_back(genInterval);
				for (int j = i+1; j < intervals.size(); j++) {
					ret.push_back(intervals[j]);
				}
			}
			return ret;
		}
		return ret;
    }
};

int main (int argc, char const *argv[])
{
	Solution sol;
	vector<Interval> v;
	Interval i0(0, 5);
	Interval i1(8, 9);
	v.push_back(i0);
	v.push_back(i1);
	Interval newInterval(3, 4);
	vector<Interval> ret = sol.insert(v, newInterval);
	for (vector<Interval>::iterator iter = ret.begin(); iter != ret.end(); iter++) {
		cout << iter->start << " " << iter->end << endl;
	}
	return 0;
}