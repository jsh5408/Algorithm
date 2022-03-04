## 11866. 요세푸스 문제 0 - C++
https://www.acmicpc.net/problem/11866

#### 내 풀이 - 성공
```
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>

#define MAXN 1005

using namespace std;

int N, K;
int ans[MAXN];
int idx;

struct Node {
	int num;
	Node* next;
};

Node Circle[MAXN];
int circleCnt;
Node* head;

Node* createNode(int n) {
	Node newNode = { n, nullptr };
	Circle[circleCnt++] = newNode;
	return &Circle[circleCnt - 1];
}

void insertNode(int n) {
	Node* newNode = createNode(n);
	if (circleCnt < 2) return;
	Circle[circleCnt - 2].next = &Circle[circleCnt - 1];
}

void deleteNode(Node* prev) {
	Node* Del = prev->next;
	prev->next = Del->next;
}

void func() {
	insertNode(-1);
	head = &Circle[0];
	for (int i = 1; i < N + 1; i++) {
		insertNode(i);
	}
	Circle[N].next = head;
	Node* tmp = head;
	while (idx < N) {
		for (int i = 1; i < K; i++) {
			tmp = tmp->next;
			if (tmp == head) tmp = tmp->next;
		}
		if (tmp->next == head) {
			tmp = head;
		}
		ans[idx++] = tmp->next->num;
		deleteNode(tmp);
	}
}

int main()
{
	//freopen("sample_input.txt", "r", stdin);

	scanf("%d %d", &N, &K);
	idx = 0; circleCnt = 0;

	func();

	printf("<");
	for (int i = 0; i < N - 1; i++) {
		printf("%d, ", ans[i]);
	}
	printf("%d>", ans[N - 1]);

	return 0;
}
```
원형큐를 생각하며 Linked List를 사용했다.
이 때, 노드들은 메모리풀을 이용해서 만들었다.

createNode) 단순 노드 생성
insertNode) 노드를 생성해서 이전 노드와 연결
deleteNode) 노드간 연결 변경

func)
가장 앞을 가리키는 head와 1 ~ N까지의 노드들을 만든다.
insertNode에서 노드끼리 연결을 해주고 맨마지막 노드는 다시 head를 가리키도록 설정했다.
=> 꼬리잡기 하듯이 원형으로 가리키게 됨

요세푸스 순열은 N개이므로 ans 배열이 N개 찰 때 까지 while문을 돌려줬다.
제거할 노드의 이전 노드를 가리키도록 설정했기 때문에 tmp를 K-1번 next로 이동해줬다.
이 때, head는 건너뛰도록 조건을 걸어주었다.

또한, 제거해야할 노드가 head가 되는 것을 방지하는 조건도 추가해줬다.
ans에 값을 넣고 나면 deleteNode를 통해 연결을 끊어주었다.

![](https://images.velog.io/images/jsh5408/post/ca46b39c-40c9-4b7f-ae2e-d025b20a63c3/image.png)