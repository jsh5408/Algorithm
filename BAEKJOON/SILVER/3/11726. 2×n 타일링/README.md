## 11726. 2×n 타일링
https://www.acmicpc.net/problem/11726

#### Brute Force - 시간초과
```
#include <stdio.h>
#include <iostream>

#define MAXN 1005

int n;
int answer;
int box[2][MAXN];

void func(int idx, int cnt)
{
	if(idx == n) {
		answer++;
		return;
	}

	int i = idx;

	if(i < n-1) {
		if(box[0][i] == 0) {
			// 세로
			box[0][i] = 1;
			box[1][i] = 1;
			func(idx+1, cnt+1);
			box[0][i] = 0;
			box[1][i] = 0;

			// 가로
			box[0][i] = 1;
			box[0][i+1] = 1;
			func(idx, cnt+1);
			box[0][i] = 0;
			box[0][i+1] = 0;
		}
		else if(box[1][i] == 0) {
			// 가로
			box[1][i] = 1;
			box[1][i+1] = 1;
			func(idx+2, cnt+1);
			box[1][i] = 0;
			box[1][i+1] = 0;
		}
	}
	else {
		if(box[0][i] == 0) {
			// 세로
			box[0][i] = 1;
			box[1][i] = 1;
			func(idx+1, cnt+1);
			box[0][i] = 0;
			box[1][i] = 0;
		}
		else if(box[1][i] == 0) {
			return;
		}
	}
}

int main()
{
	//freopen("input.txt", "r", stdin);

	scanf("%d", &n);

	func(0, 0);

	printf("%d", answer % 10007);

	return 0;
}
```
직접 2 * n의 직사각형을 만들어서 1 * 2, 2 * 1 직사각형으로 직접 채워보기
-> 역시나 시간초과였다.

다음 방법으로 생각한 것은 DP 이용하기
따라서 규칙 먼저 찾아보니까 N 번째 값은 N-2 번째와 N-1 번째의 합이더라.
피보나치를 써보자!!

#### 재귀 - 시간초과
```
#include <stdio.h>
#include <iostream>

#define MAXN 1005

int n;
int answer;
int num[3];

int func(int N)
{
	if(N < 3) {
		return num[N-1] % 10007;
	}
	return (func(N-2) + func(N-1)) % 10007;
}

int main()
{
	//freopen("input.txt", "r", stdin);

	scanf("%d", &n);
	
	num[0] = 1;
	num[1] = 2;
	num[2] = 3;

	answer = func(n);

	printf("%d", answer % 10007);

	return 0;
}
```
제일 기본적인 재귀를 이용한 피보나치
-> 시간초과였다

#### DP - 성공
```
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
```
DP 값을 사용한 재귀로 변경하니까 통과됐다!

이미 구한 값은 DP 값을 사용하고
아직 구하지 않은 값은 재귀를 돌려줬다.

![](https://media.vlpt.us/images/jsh5408/post/d1065623-2bf3-4b9b-b399-04c1f704e657/image.png)