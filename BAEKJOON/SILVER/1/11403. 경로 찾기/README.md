## 11403. 경로 찾기 - C++
https://www.acmicpc.net/problem/11403

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

#define MAXN 105

using namespace std;

int N, K;
int Graph[MAXN][MAXN];
int ans[MAXN][MAXN];
vector<int> node[MAXN];
queue<int> q;
int tmp;

int main()
{
	//freopen("sample_input.txt", "r", stdin);

	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &Graph[i][j]);
			ans[i][j] = 0;
			if (Graph[i][j]) {
				ans[i][j] = 1;
				node[i].push_back(j);
			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < node[i].size(); j++) {
			q.push(node[i][j]);
		}
		while (!q.empty()) {
			tmp = q.front();
			q.pop();
			ans[i][tmp] = 1;
			for (int j = 0; j < node[tmp].size(); j++) {
				if (ans[i][node[tmp][j]] == 0)
					q.push(node[tmp][j]);
			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			printf("%d ", ans[i][j]);
		}
		printf("\n");
	}

	return 0;
}
```
Graph 를 입력 받으면서 i -> j 경로가 있는 1 일 때만 node[i] 에 j 들을 push & ans = 1

0 ~ N 까지의 정점들을 보면서 i 와 연결된 node 값들을 q 에 모두 push
q 의 값들을 하나씩 pop 하면서 해당 값과 연결된 정점들도 모두 q 에 저장
q 에 저장된 애들은 모두 i 와 연결된 애들이니까 ans 값 = 1

ans 값들은 한번에 출력

![](https://images.velog.io/images/jsh5408/post/4ee6159f-e90a-4731-b1f9-c6dd9dd9bee3/image.png)