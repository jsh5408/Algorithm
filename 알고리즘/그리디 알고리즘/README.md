: 매 선택에서 지금 이 순간 당장 최적인 답을 선택하여 적합한 결과를 도출하자
= 욕심쟁이 알고리즘, 탐욕 알고리즘

- **최적화**

* 장점: 빠르다
* 단점: **항상 최적이라는 보장은 없음**

---

## 1. 최소 신장 트리

#### 신장 트리
: n 개의 정점으로 이루어진 무방향 그래프 G 에서 n 개의 모든 정점과 n-1 개의 간선으로 만들어진 트리 (최소의 간선으로 모든 정점을 연결한 그래프)

#### 최소 신장 트리 (MST, Minimum Spanning Tree)
: 가중치의 합이 최소인 신장 트리

#### 최소 신장 트리를 찾는 대표적인 그리디 알고리즘
크루스칼 알고리즘 (Kruskal's Algorithm)
프림 알고리즘 (Prim's Algorithm)

---

### 크루스칼 알고리즘 (Kruskal's Algorithm)

1. 가중치 순서대로 오름차순 정렬하기
2. 정렬된 간선을 순서대로 선택
3. 선택한 간선이 사이클을 이루지 않으면 연결해서 트리에 추가
4. 사이클이 된다면 버림

* **O(ElogE)**
* 간선이 적은 경우에 적합

* 참고) **Union-Find 알고리즘**

* Python 코드
```
mygraph = {

'vertices':['A','B','C','D','E','F','G'],
'edges':[

     (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}
```
```
parent = dict()
rank = dict()

def find(node):
    # parent compression 기법
    if parent[node] != node:
           parent[node] = find(parent[node])
       return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)
    # union by rank 기법
    if rank[root1]> rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2]+=1


def make_set(node):
    parent[node] = node
    rank[node] =0

def kruskal(graph):
    mst = list()
    # 1. 초기화
    for node in graph['vertices']:
        make_set(node)

    # 2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    # 3. 간선 연결 (사이클 없는)
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)
     return mst
```
```
kruskal(mygraph)
"""
[(5, 'A', 'D'),
 (5, 'C', 'E'),
 (6, 'D', 'F'),
 (7, 'A', 'B'),
 (7, 'B', 'E'),
 (9, 'E', 'G')]
"""
```

>[크루스칼 알고리즘 참고]
(https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html)
[크루스칼 알고리즘 Python]
(https://kils-log-of-develop.tistory.com/256)

---

### 프림 알고리즘 (Prim's Algorithm)

1. 그래프에서 하나의 정점을 선택하여 트리 생성
2. 그래프의 모든 간선이 들어 있는 집합 생성
3. 모든 정점이 트리에 포함될 때까지, 트리와 연결된 간선 가운데 사이클이 없고 가장 가중치가 작은 간선을 트리에 추가

* **Min-Heap: O(ElogE) / 최악 O(n^2)**
* 간선이 많은 경우에 적합

* Python 코드
```
myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]
```
```
from collections import defaultdict
from heapq import *

def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)

    return mst
```
```
prim ('A', myedges)
"""
[(5, 'A', 'D'),
 (6, 'D', 'F'),
 (7, 'A', 'B'),
 (7, 'B', 'E'),
 (5, 'E', 'C'),
 (9, 'E', 'G')]
"""
```

> [프림 알고리즘 참고]
(https://gmlwjd9405.github.io/2018/08/30/algorithm-prim-mst.html)
[프림 알고리즘 Python]
(https://kils-log-of-develop.tistory.com/263)

---

## 2. 최단 경로

#### 최단 경로를 찾는 가장 대표적인 그리디 알고리즘
다익스트라 알고리즘 (Dijkstra Algorithm)

---

### 다익스트라 알고리즘 (Dijkstra Algorithm)
: 음의 가중치가 없는 그래프의 한 정점에서 모든 정점까지의 최단거리를 구하는 알고리즘

* 그래프 방향의 유무는 상관 없으나, 가중치가 음수면 안됨

* **초기: O(n^2) / 우선순위 큐 (Min-Heap): O(E + ElogE) = O(ElogE)**

* Python 코드 - **최단 거리 출력**
```
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
```
```
import heapq

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances
```
```
dijkstra(mygraph, 'A')
"""
{'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}
"""
```

* Python 코드 - **최단 경로 출력**
```
import heapq

def dijkstra(graph, start, end):

    distances = {vertex: [float('inf'), start] for vertex in graph}
    # 그래프의 시작 정점의 거리는 0 으로 초기화
    distances[start] = [0, start]
    # 큐 => 모든 정점을 저장
    queue = []
    # 그래프의 시작 정점과 시작 정점의 거리(0) 을 최소힙에 넣어줌
    heapq.heappush(queue, [distance[start][0], start])

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        # 더 짧은 경로가 있다면 무시
        if distances[current_vertex][0] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # 시작 -> 인접으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우
            if distance < distances[adjacent][0]:
                # 거리 업데이트
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])
                
    path = end
    path_output = end + '->'
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]
    path_output += start
    print(path_output)
    return distances
```
```
print(dijkstra(mygraph, 'A', 'F'))
"""
F->E->D->A

{'A': [0, 'A'],
 'B': [6, 'C'],
 'C': [1, 'A'],
 'D': [2, 'A'],
 'E': [5, 'D'],
 'F': [6, 'E']}
"""
```

> [다익스트라 알고리즘 참고]
(https://mattlee.tistory.com/50)
[다익스트라 알고리즘 Python]
(https://www.fun-coding.org/Chapter20-shortest-live.html)

---

## 3. 허프만 코드 (Huffman Code)

: 많이 쓰이는 문자에는 작은 비트를 할당하고 적게 쓰이는 문자에는 큰 비트를 할당하여
최소의 비트로 데이터(문자)를 압축하는 방식

- **Min-Heap** 이용

> [허프만 코드 참고]
(https://lipcoder.tistory.com/187)