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