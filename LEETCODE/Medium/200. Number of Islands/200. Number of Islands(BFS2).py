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