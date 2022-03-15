## 11724. 연결 요소의 개수 - C++
https://www.acmicpc.net/problem/11724

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

#define MAXN 1005

using namespace std;

int N, M, u, v;
vector<int> graph[MAXN];
int ans;
int visited[MAXN];

void func(int node) {
	if (visited[node]) return;
	visited[node] = 1;

	for (int i = 0; i < graph[node].size(); i++) {
		func(graph[node][i]);
	}
}

int main()
{
	//freopen("sample_input.txt", "r", stdin);

	scanf("%d %d", &N, &M);

	for (int i = 0; i < M; i++) {
		scanf("%d %d", &u, &v);
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	for (int i = 1; i < N + 1; i++) {
		if (visited[i] == 0) {
			func(i);
			ans++;
		}
	}

	printf("%d", ans);

	return 0;
}
```
무방향이기 때문에 입력받은 u, v 에 대해 양방향 연결
=> graph[u] 에 v 추가, graph[v] 에 u 추가

visited 를 이용해서 특정 노드와 연결된 모든 노드들은 visited = 1 하며 모든 노드 확인
func 을 돌 때마다 하나의 연결이 생기는 것이므로 ans++

![](https://images.velog.io/images/jsh5408/post/cd97baaa-525d-444c-90e1-73622aa432a7/image.png)