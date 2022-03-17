#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>
#include <set>

#define INF 987654321
#define MAXN 505

using namespace std;

int N, M, B, num;
unordered_map<int, int> heights;
set<int> nums;
int ans[2];

int func(int target, int b)
{
	int total = 0;
	for (auto iter = nums.rbegin(); iter != nums.rend(); iter++) {
		int n = *iter;
		int tmp = 0;
		// 블록 제거
		if (n > target) {
			int h = n - target;
			tmp = 2 * heights[n] * h;
			b += heights[n] * h;
			n = target;
		}
		// 블록 추가
		else if (n < target) {
			// 인벤토리 내에서 해결 가능한지 확인
			int h = target - n;
			if (h * heights[n] <= b) {
				tmp = heights[n] * h;
				b -= heights[n] * h;
				n = target;
			}
			else {
				return INF;
			}
		}
		total += tmp;
	}

	return total;
}

int main()
{
	//freopen("sample_input.txt", "r", stdin);

	scanf("%d %d %d", &N, &M, &B);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%d", &num);
			heights[num] += 1;
			nums.insert(num);
		}
	}

	ans[0] = INF;

	for (int i = 0; i <= 256; i++) {
		int tmp = func(i, B);
		if (ans[0] >= tmp) {
			ans[0] = tmp;
			ans[1] = i;
		}
	}

	printf("%d %d", ans[0], ans[1]);

	return 0;
}