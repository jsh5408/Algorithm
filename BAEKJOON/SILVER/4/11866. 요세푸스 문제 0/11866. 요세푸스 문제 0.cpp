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