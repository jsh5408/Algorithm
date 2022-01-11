#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define MAXLEN 501
#define INF 987654321

int N, M;
int a, b, c;
int ans;
int dp[MAXLEN][MAXLEN];

int main()
{
	scanf("%d %d", &N, &M);

	for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            dp[i][j] = INF;
        }
    }

	for(int i=0;i<M;i++) {
		scanf("%d %d", &a, &b);
		dp[a][b] = 0;
	}

	for (int k = 1; k <= N; k++) {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (i == j) continue;
                if (dp[i][k] == INF || dp[k][j] == INF) continue;
                if (dp[i][j] >= dp[i][k] + dp[k][j]) dp[i][j] = dp[i][k] + dp[k][j];
            }
        }
    }

	for(int i=1; i<=N; i++) {
		int cnt = 0;
		for (int j = 1; j <= N; j++) {
			if(dp[i][j]==0) {
				cnt += 1;
			}
		}
		for (int j = 1; j <= N; j++) {
			if(dp[j][i]==0) {
				cnt += 1;
			}
		}
		if(cnt == N-1) {
			ans += 1;
		}
	}

	printf("%d", ans);

	return 0;
}