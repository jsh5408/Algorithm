#include <stdio.h>
#include <iostream>

#define MAXN 1005

using namespace std;

int N;
int nums[MAXN];
int ans;

int main()
{
	//freopen("input.txt", "r", stdin);

	scanf("%d", &N);

	nums[0] = 0;
	nums[1] = 1;
	nums[2] = 3;

	for (int i = 3; i <= N; i++) {
		nums[i] = (nums[i - 1] + nums[i - 2] * 2) % 10007;
	}

	printf("%d", nums[N]);

	return 0;
}