Python 참고: http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-2.html

#### 깊이 우선 탐색 (Depth-First Search: DFS)
: 루트 노드부터 내려갈 수 있는 만큼 깊이 탐색 (세로->가로)

**<가장 대표적인 DFS - 전위 pre-order>**
```
def _pre_order_traversal(root):
     if root is None:
          pass
     else:
          print(root.data)
          _pre_order_traversal(root.left)
          _pre_order_traversal(root.right)
```
root -> 왼쪽 -> 오른쪽

**<정위 in-order>**
```
def _in_order_traversal(root):
     if root is None:
          pass
     else:
          _in_order_traversal(root.left)
          print(root.data)
          _in_order_traversal(root.right)
```
왼쪽 -> root -> 오른쪽

**<후위 post-order>**
```
def _post_order_traversal(root):
     if root is None:
          pass
     else:
          _post_order_traversal(root.left)
          _post_order_traversal(root.right)
          print(root.data)
```
왼쪽 -> 오른쪽 -> root

#### 너비 우선 탐색 (Breadth-First Search: BFS)
: 같은 레벨끼리 탐색 (가로->세로)
```
def _level_order_traversal(root):
     queue = [root]
     while queue:
          root = queue.pop(0)
          if root is not None:
              print(root.data)
              if root.left:
                  queue.append(root.left)
              if root.right:
                  queue.append(root.right)
```
큐를 이용해서 왼쪽 오른쪽 값을 순서대로 append