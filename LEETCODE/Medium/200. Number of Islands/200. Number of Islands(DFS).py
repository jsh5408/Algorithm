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