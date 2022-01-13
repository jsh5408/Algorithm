#include <iostream>
#include <string.h>
#include <queue>
#include <vector>

using namespace std;

#define MAXLEN 501
#define INF 987654321

int n, m;
int triangle[MAXLEN][MAXLEN];
int dp[MAXLEN][MAXLEN];

int main() {

	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			scanf("%d", &triangle[i][j]);
		}
	}

	for (int i = 0; i <= n; i++) {
		for (int j = 0; j <= n; j++) {
			dp[i][j] = 0;
		}
	}

	dp[1][1] = triangle[1][1];

	for (int i = 2; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]);
			dp[i][j] += triangle[i][j];
		}
	}

	m = 0;

	for (int i = 0; i <= n; i++) {
		if (m < dp[n][i]) {
			m = dp[n][i];
		}
	}

	printf("%d", m);

	return 0;
}