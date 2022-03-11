## 15829. Hashing - C++
https://www.acmicpc.net/problem/15829

#### 내 풀이 - 성공
```
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

#define MAXN 105
#define M 1234567891
#define r 31

using namespace std;

int L;
string str;
long long ans;

int main()
{
	//freopen("sample_input.txt", "r", stdin);

	cin >> L;
	cin >> str;

	ans = 0;
	long long rr = 1;

	for (int i = 0; i < L; i++) {
		ans = (ans + (str[i] - 'a' + 1) * rr) % M;
		rr = (rr * r) % M;
	}

	cout << ans;

	return 0;
}
```
![](https://images.velog.io/images/jsh5408/post/f80830c8-45eb-42a6-8c49-18015e26f272/image.png)

여기서 중요한 것은 MOD 이다.

1 <= L <= 5 의 범위인 SMALL(50점) 까지는 크게 신경 쓰지 않아도 통과 가능하지만
1 <= L <= 50 의 범위인 Large(50점) 까지는 MOD 를 주의해야한다.

a * r 을 더할 때마다 MOD 를 해줘야하며
31 의 배수도 급격히 커지기 때문에 MOD 가 필요하다.
이 때, 둘 다 기존의 ans 값과 rr 값을 포함해서 MOD 해야한다.

포함하지 않는 경우
```
ans += ((str[i] - 'a' + 1) * rr) % M;
rr *= r % Mod;
```
=> X

> **비둘기집의 원리**
n 개의 비둘기집과 n+1 마리의 비둘기가 있다고 가정한다.
>
만약 각 비둘기집에 한 마리 이하의 비둘기만 들어 있다면,
전체 비둘기집에는 많아야 n 마리의 비둘기가 존재한다.
>
그런데 비둘기는 모두 n+1 마리이므로, 이것은 모순이다.
따라서 어느 비둘기집에는 두 마리 이상의 비둘기가 있다.
>
* 해시 충돌
: 해시 테이블에서 가능한 모든 키의 숫자는 테이블 인덱스의 개수보다 많으므로 충돌은 불가피하다. 따라서 어떤 해시 함수도 충돌을 피할 수는 없다.
>
[위키백과](https://ko.wikipedia.org/wiki/%EB%B9%84%EB%91%98%EA%B8%B0%EC%A7%91_%EC%9B%90%EB%A6%AC)

![](https://images.velog.io/images/jsh5408/post/a864ed58-4a55-4925-99cb-dea321d7dde2/image.png)