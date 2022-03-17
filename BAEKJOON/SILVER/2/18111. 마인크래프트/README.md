## 18111. 마인크래프트 - C++
https://www.acmicpc.net/problem/18111

#### 내 풀이 - 성공
```
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
```
처음에는 최소 시간을 구해야한다는 것에 어렵게 접근했지만 브루트포스로 충분히 풀 수 있는 문제였다

좌표가 중요한 역할을 하진 않아서 높이의 개수를 unordered_map 에 저장해줬다
또한 높이들은 set 에 저장해서 순서대로 접근할 수 있도록 했다

0 ~ 256 까지의 모든 경우를 target 으로 삼고 걸리는 시간을 구했다
인벤토리의 여유를 미리 확보해두기 위해 높이가 큰 애들부터 블록 제거를 했다

조절해야 하는 길이 * 같은 높이의 개수 * 걸리는 시간(1 or 2) 를 모두 더해서 return
인벤토리의 블록이 부족하면 불가능한 경우니까 INF 를 return

최솟값으로 갱신해주고 같은 시간이면 더 높은 높이로 갱신해줬다

![](https://images.velog.io/images/jsh5408/post/cfa99779-74f7-48dc-9bb1-ca78ebf371d8/image.png)