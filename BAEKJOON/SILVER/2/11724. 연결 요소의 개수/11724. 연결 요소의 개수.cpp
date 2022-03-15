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