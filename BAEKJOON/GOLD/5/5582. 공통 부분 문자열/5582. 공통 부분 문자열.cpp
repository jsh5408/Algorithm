#include <iostream>
#include <string.h>
#include <queue>
#include <vector>

using namespace std;

#define MAXLEN 4001
#define INF 987654321

int N, M, a, b, c, d;
int dp[MAXLEN][MAXLEN];
char A[MAXLEN];
char B[MAXLEN];

int main() {

	scanf("%s", &A);
	scanf("%s", &B);

	int m = 0;

	for(int i=0;i<strlen(A);i++) {
		for(int j=0;j<strlen(B);j++) {
			if(A[i] == B[j]) {
				dp[i][j] = 1;
				if(i > 0 && j > 0) dp[i][j] += dp[i-1][j-1];
				m = max(m, dp[i][j]);
			}
		}
	}

	printf("%d", m);

	return 0;
}