#include <iostream>
#include <string.h>
#include <queue>
#include <vector>

using namespace std;

#define MAXLEN 1025
#define INF 987654321

int N, M, a, b, c, d;
long dp[MAXLEN][MAXLEN];

int main() {

	scanf("%d %d", &N, &M);

	for(int i=0;i<=N;i++) {
		for(int j=0;j<=N;j++) {
			dp[i][j] = 0;
		}
	}

	for(int i=1;i<=N;i++) {
		for(int j=1;j<=N;j++) {
			scanf("%d", &a);
			dp[i][j] = a;
		}
	}

	for(int i=1;i<=N;i++) {
		for(int j=1;j<=N;j++) {
			dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + dp[i][j];
		}
	}

	for(int i=0;i<M;i++) {
		scanf("%d %d %d %d", &a, &b, &c, &d);
		printf("%d\n", dp[c][d] - dp[a-1][d] - dp[c][b-1] + dp[a-1][b-1]);
	}

	return 0;
}