#include <bits/stdc++.h>
using namespace std;

int N, K;
int DP[10+1][10+1];

int main()
{
	scanf("%d %d", &N, &K);
	
	DP[0][0] = 1;
	for(int i=1;i<=N;i++) {
	    DP[i][0] = 1;
	    for(int j=1;j<=i;j++) {
	        DP[i][j] = DP[i-1][j-1] + DP[i-1][j];
	    }
	}
	
	printf("%d", DP[N][K]);

	return 0;
}