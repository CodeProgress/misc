
#include "stdafx.h"
#include <cmath>
#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main()
{
	high_resolution_clock::time_point t1 = high_resolution_clock::now();
	int oneBillion = pow(10, 9);
	long long x = 0;
	cout << "Hello\n";
	for (auto i = 0; i <= oneBillion; i++) {
		x += i;
	}
	//cout << x;

	high_resolution_clock::time_point t2 = high_resolution_clock::now();

	auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();

	cout << duration << " milliseconds";

	cin.ignore();
    return 0;
}

