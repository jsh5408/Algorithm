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