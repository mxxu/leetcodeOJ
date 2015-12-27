#include <iostream>

using namespace std;

int main (int argc, char const *argv[])
{
	cout << std::numeric_limits<int>::max() << endl;
	cout << std::numeric_limits<int>::min() << endl;
	int a = std::numeric_limits<int>::max();
	cout << a + 1 << endl;
	int b = 1032666230;
	cout << b * 10 << endl;
	if (a * 10 < a) {
		cout << "wtf\n";
	}
	return 0;
}