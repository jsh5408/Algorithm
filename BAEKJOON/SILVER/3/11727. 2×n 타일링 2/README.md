## 11727. 2×n 타일링 2
https://www.acmicpc.net/problem/11727

#### DP - 성공
```
#include <stdio.h>
#include <iostream>

#define MAXN 1005

using namespace std;

int N;
int nums[MAXN];
int ans;

int main()
{
	//freopen("input.txt", "r", stdin);

	scanf("%d", &N);

	nums[0] = 0;
	nums[1] = 1;
	nums[2] = 3;

	for (int i = 3; i <= N; i++) {
		nums[i] = (nums[i - 1] + nums[i - 2] * 2) % 10007;
	}

	printf("%d", nums[N]);

	return 0;
}
```
![](https://media.vlpt.us/images/jsh5408/post/843c0f1a-d571-4570-b106-1c40b216f254/image.png)

11726번 문제에서 응용해서 적절한 점화식을 찾아주었다.

2 x 2 의 사각형이 추가됐으므로 2 x 2 크기를 채울 사각형은 2 가지가 된다.
=> `nums[i-2] * 2` 를 해줬다.

![](https://media.vlpt.us/images/jsh5408/post/d7c438aa-55d8-4142-8f6d-606c17e1388b/image.png)