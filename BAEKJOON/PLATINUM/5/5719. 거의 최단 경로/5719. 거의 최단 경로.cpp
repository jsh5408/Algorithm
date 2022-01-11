#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define MAXLEN 501
#define INF 987654321

struct Data {
	int node, weight;
	Data() {};
	Data(int node, int weight) : node(node), weight(weight) {};
	bool operator<(const Data d) const {
		return weight > d.weight;
	}
};

int N, M, S, D, U, V, P;
vector<Data> v[MAXLEN];
int dist[MAXLEN];
vector<int> parent[MAXLEN];
bool isVisited[MAXLEN];
priority_queue<Data> pq;

bool mat[MAXLEN][MAXLEN];

void recursion(int child) {
	if(child == S) return;

	for(int i=0; i<parent[child].size(); i++) {
		if(mat[parent[child][i]][child]) continue;
		mat[parent[child][i]][child] = true;
		recursion(parent[child][i]);
	}
}

int main()
{
	while(true) {
		scanf("%d %d", &N, &M);
		if(N == 0 && M == 0) break;

		scanf("%d %d", &S, &D);

		for(int i=0;i<=N;i++) {
			v[i].clear();
			dist[i] = INF;
			isVisited[i] = false;
		}

		for(int i=0;i<=N;i++) {
			for(int j=0;j<=N;j++) {
				mat[i][j] = false;
			}
		}

		for(int i=0;i<M;i++) {
			scanf("%d %d %d", &U, &V, &P);
			v[U].push_back(Data(V, P));	// a -> b 의 경우 저장
		}

		dist[S] = 0;
		pq.push(Data(S,0));

		while(true) {
			if(pq.empty()) break;
			Data now = pq.top();
			pq.pop();

			if(isVisited[now.node]) continue;
			isVisited[now.node] = true;

			for(int i=0; i<v[now.node].size(); i++) {
				Data next = v[now.node].at(i);
				if(dist[next.node] > dist[now.node] + next.weight) {
					parent[next.node].clear();
					parent[next.node].push_back(now.node);
					dist[next.node] = dist[now.node] + next.weight;
					pq.push(Data(next.node, dist[next.node]));
				}
				else if(dist[next.node] == dist[now.node] + next.weight) {
					parent[next.node].push_back(now.node);
				}
			}
		}

		recursion(D);

		for(int i=0;i<=N;i++) {
			dist[i] = INF;
			isVisited[i] = false;
		}

		dist[S] = 0;
		pq.push(Data(S,0));

		while(true) {
			if(pq.empty()) break;
			Data now = pq.top();
			pq.pop();

			if(isVisited[now.node]) continue;
			isVisited[now.node] = true;

			for(int i=0; i<v[now.node].size(); i++) {
				Data next = v[now.node].at(i);
				if(mat[now.node][next.node]) continue;
				if(dist[next.node] > dist[now.node] + next.weight) {
					dist[next.node] = dist[now.node] + next.weight;
					pq.push(Data(next.node, dist[next.node]));
				}
			}
		}

		if(dist[D] == INF) dist[D] = -1;

		printf("%d\n", dist[D]);
	}

	return 0;
}