## 14500. 테트로미노
https://www.acmicpc.net/problem/14500

#### Brute Force - 성공
```
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
```
N, M 이 500 이하기 때문에 Brute Force 로 충분히 풀 수 있었다.

모든 숫자마다 연속된 4 개의 숫자들의 합 중 최댓값을 확인하도록 했다.
핵심은 ㅗ, ㅜ, ㅓ, ㅏ 처럼 가운데에 붙는 경우를 별도로 처리해줘야한다는 점이다.
따라서 cnt == 2 일 때는 직접 더해서 최댓값인지 확인하도록 해줬다.

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/1d81e790-8b38-4648-0c58-dbb3ef9f4300/public)
