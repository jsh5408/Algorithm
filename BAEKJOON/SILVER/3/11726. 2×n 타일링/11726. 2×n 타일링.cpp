#include <stdio.h>
#include <iostream>

#define MAXN 1005

int n;
int answer;
int num[MAXN];

int func(int N)
{
	if(N < 3) {
		num[N] = num[N] % 10007;
	}
    else if(num[N-2] && num[N-1]) {
		num[N] = (num[N-2] + num[N-1]) % 10007;
	}
	else if(num[N-2]) {
		num[N] = (num[N-2] + func(N-1)) % 10007;
	}
	else if(num[N-1]) {
		num[N] = (func(N-2) + num[N-1]) % 10007;
	}
	else {
		num[N] = (func(N-2) + func(N-1)) % 10007;
	}
	return num[N];
}

int main()
{
	//freopen("input.txt", "r", stdin);

	scanf("%d", &n);
	
	num[0] = 0;
	num[1] = 1;
	num[2] = 2;

	answer = func(n);

	printf("%d", answer % 10007);

	return 0;
}