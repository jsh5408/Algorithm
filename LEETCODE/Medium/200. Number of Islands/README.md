https://leetcode.com/problems/number-of-islands/

#### DFS - 성공
```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def func(i, j):
            grid[i][j] = "0"
            if i > 0 and grid[i-1][j] == "1":
                func(i-1, j)
            if j > 0 and grid[i][j-1] == "1":
                func(i, j-1)
            if i < len(grid)-1 and grid[i+1][j] == "1":
                func(i+1, j)
            if j < len(grid[0])-1 and grid[i][j+1] == "1":
                func(i, j+1)
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    ans += 1
                    func(i, j)
        
        return ans
```
1 을 만나면 해당 1 과 연결된 모든 1 들을 0 으로 바꿔주면서 count

주의할 점은 string 숫자로 저장되어있다는 점이다

![](https://velog.velcdn.com/images/jsh5408/post/cb934c0a-2da5-4b53-b054-f14921e5e2dd/image.png)

#### BFS - 성공
```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    ans += 1
                    q.append([i, j])
                    grid[i][j] = "0"
                    
                    while q:
                        ii, jj = q.pop()
                        grid[ii][jj] = "0"
                        if ii > 0 and grid[ii-1][jj] == "1":
                            q.append([ii-1, jj])
                        if jj > 0 and grid[ii][jj-1] == "1":
                            q.append([ii, jj-1])
                        if ii < len(grid)-1 and grid[ii+1][jj] == "1":
                            q.append([ii+1, jj])
                        if jj < len(grid[0])-1 and grid[ii][jj+1] == "1":
                            q.append([ii, jj+1])
                    
        return ans
```
1 을 만나면 해당 좌표를 q 에 넣고 상하좌우를 확인해서 연결된 1 들도 모두 q 에 넣음

큐를 이용한 BFS 가 더 빠르다
> 실제로 코테에서 DFS 로 런타임 에러가 났었는데 BFS 로 바꾸니까 통과된 적이 있다!

![](https://velog.velcdn.com/images/jsh5408/post/034ad211-6543-41c6-a445-511f5baf5300/image.png)

#### BFS - 성공
```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        q = []
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    ans += 1
                    q.append([i, j])
                    
                    while q:
                        ii, jj = q.pop()
                        grid[ii][jj] = "0"
                        for k in range(4):
                            ni = ii + direction[k][0]
                            nj = jj + direction[k][1]
                            if ni < 0 or nj < 0 or ni >= len(grid) or nj >= len(grid[0]):
                                continue
                            if grid[ni][nj] == "1":
                                q.append([ni, nj])
                    
        return ans
```
상하좌우를 direction 리스트를 이용해 확인하는 방법
더 깔끔하게 작성할 수 있다

![](https://velog.velcdn.com/images/jsh5408/post/cf4b00d3-0779-4e41-b13c-cc0bbb9b0786/image.png)
