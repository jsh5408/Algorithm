#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>

using namespace std;

int main()
{
	long X, Y;
	scanf("%d %d", &X, &Y);

	int Z = (Y * 100 / X);

	if(Z >= 99) {
		printf("-1");
		return 0;
	}

	int left = 0, right = 1000000000;

	while(left <= right) {
		int mid = (left + right) / 2;
		int tmp = ((Y+mid)*100 / (X+mid));

		if(tmp > Z) {
			right = mid-1;
		}
		else {
			left = mid+1;
		}
	}

	printf("%d", left);

	return 0;
}