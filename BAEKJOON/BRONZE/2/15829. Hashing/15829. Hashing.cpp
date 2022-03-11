#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

#define MAXN 105
#define M 1234567891
#define r 31

using namespace std;

int L;
string str;
long long ans;

int main()
{
	//freopen("sample_input.txt", "r", stdin);

	cin >> L;
	cin >> str;

	ans = 0;
	long long rr = 1;

	for (int i = 0; i < L; i++) {
		ans = (ans + (str[i] - 'a' + 1) * rr) % M;
		rr = (rr * r) % M;
	}

	cout << ans;

	return 0;
}