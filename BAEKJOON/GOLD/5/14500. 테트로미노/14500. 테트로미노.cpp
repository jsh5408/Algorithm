#include <iostream>
#include <stdio.h>
#include <algorithm>

#define INF 987654321
#define MAXN 505

using namespace std;

int N, M;
int nums[MAXN][MAXN];
int visited[MAXN][MAXN];
int ans;

void func(int i, int j, int cnt, int total, int dir)
{
	if (cnt == 4) {
		ans = max(ans, total);
		return;
	}

	visited[i][j] = 1;

	int a = 0, b = 0, c = 0, d = 0;
	if (i > 0 && visited[i - 1][j] == 0) {
		func(i - 1, j, cnt + 1, total + nums[i - 1][j], 1);
		a = nums[i - 1][j];
	}
	if (j > 0 && visited[i][j - 1] == 0) {
		func(i, j - 1, cnt + 1, total + nums[i][j - 1], 2);
		b = nums[i][j - 1];
	}
	if (i < N - 1 && visited[i + 1][j] == 0) {
		func(i + 1, j, cnt + 1, total + nums[i + 1][j], 3);
		c = nums[i + 1][j];
	}
	if (j < M - 1 && visited[i][j + 1] == 0) {
		func(i, j + 1, cnt + 1, total + nums[i][j + 1], 4);
		d = nums[i][j + 1];
	}

	if (cnt == 2) {
		switch (dir) {
		case 1:
			ans = max(ans, total + a + d);
			ans = max(ans, total + a + b);
			break;
		case 2:
			ans = max(ans, total + a + b);
			ans = max(ans, total + b + c);
			break;
		case 3:
			ans = max(ans, total + c + d);
			ans = max(ans, total + b + c);
			break;
		case 4:
			ans = max(ans, total + a + d);
			ans = max(ans, total + c + d);
			break;
		}
	}

	visited[i][j] = 0;
}

int main()
{
	//freopen("input.txt", "r", stdin);

	scanf("%d %d", &N, &M);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%d", &nums[i][j]);
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			func(i, j, 0, 0, 0);
		}
	}

	printf("%d", ans);

	return 0;
}