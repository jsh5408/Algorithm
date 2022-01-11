#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define MAXLEN 20001
#define INF 987654321

struct Data {
	int node, weight;
	Data() {};
	Data(int node, int weight) : node(node), weight(weight) {};
	bool operator<(const Data d) const {
		return weight > d.weight;
	}
};

int N, M, S, a, b, c;
vector<Data> v[MAXLEN];
int dist[MAXLEN];
bool isVisited[MAXLEN];
priority_queue<Data> pq;

int main()
{
	scanf("%d %d", &N, &M);
	scanf("%d", &S);

	for(int i=0;i<=N;i++) {
		v[i].clear();
		dist[i] = INF;
		isVisited[i] = false;
	}

	for(int i=0;i<M;i++) {
		scanf("%d %d %d", &a, &b, &c);
		v[a].push_back(Data(b, c));
		//v[b].push_back(Data(a, c));
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
				dist[next.node] = dist[now.node] + next.weight;
				pq.push(Data(next.node, dist[next.node]));
			}
		}
	}

	for(int i=1; i<=N; i++) {
		if(dist[i] == INF) printf("INF\n");
		else printf("%d\n", dist[i]);
	}

	return 0;
}