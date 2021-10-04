#include <iostream>
#include <cmath>
#include <typeinfo>
using namespace std;

int main()
{
	int side;
	cin >> side;
	double ans;
	ans = side * side*(sqrt(3) / 4);
	cout << typeid(ans).name() << endl;

	side = double(side);
	ans = side * side*(sqrt(3) / 4);
	printf(typeid(ans).name());
	return 0;
}